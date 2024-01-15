import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { delay } from 'rxjs/operators';
import { NgbNavModule } from '@ng-bootstrap/ng-bootstrap';

type MessageArray = { llm_bot: boolean, timestamp: string, message: string }[]
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpClient) { }

  active = "Title"
  dummy_http_request = true

  // input settings
  input = {
    product_info: {
      "TitlePlain": "",
      "DeliveryContents": "",
      "UserInstructions": "",
      "UserCustomization": ""
    },
    output_settings: {
      "Title": false,
      "DescriptionLong": false,
      "SalesArguments": false,
      "BulletPoints": false,
      "xxx": false
    }
  }

  // object for first message in chat
  direct_chat_messages_array: MessageArray = [
    {
      llm_bot: true,
      timestamp: "23 Jan 2:00 pm",
      message: "Hallo, ich bin Ihr persönlicher LLM-Assistent für die Erstellung von Produktbeschreibungen. Bitte füllen Sie oben das Formular mit den Produktmerkmalen aus und senden Sie anschließend eine Anfrage zur Generierung der Produktbeschreibung, indem Sie auf die Schaltfläche „Produktbeschreibung generieren“ klicken."
    }
  ]

  // object that stores each product, its name, id and the corresponding llm chat
  product_info_array: { product_id: string, display_name: string, message_array: MessageArray }[] = [
    { product_id: "Title", display_name: "Titel", message_array: this.direct_chat_messages_array.map(object => ({ ...object })) },
    { product_id: "DescriptionLong", display_name: "Produktbeschreibung", message_array: this.direct_chat_messages_array.map(object => ({ ...object })) },
    { product_id: "SalesArguments", display_name: "Verkaufsargumente", message_array: this.direct_chat_messages_array.map(object => ({ ...object })) },
    { product_id: "BulletPoints", display_name: "Bulletpoints", message_array: this.direct_chat_messages_array.map(object => ({ ...object })) }
  ]

  // function to set the standard for input settings
  set_std_input() {
    this.input = {
      product_info: {
        "TitlePlain": "Wandlampe",
        "DeliveryContents": "Lampenkörper",
        "UserInstructions": "10cm x 30cm",
        "UserCustomization": "Besonders freundlicher Output"
      },
      output_settings: {
        "Title": true,
        "DescriptionLong": true,
        "SalesArguments": true,
        "BulletPoints": true,
        "xxx": false
      }
    }
  }

  // function to reset input settings
  reset_input() {
    this.input = {
      product_info: {
        "TitlePlain": "",
        "DeliveryContents": "",
        "UserInstructions": "",
        "UserCustomization": ""
      },
      output_settings: {
        "Title": false,
        "DescriptionLong": false,
        "SalesArguments": false,
        "BulletPoints": false,
        "xxx": false
      }
    }
  }

  // initial call to llm
  // generates a response for each product id that was selected in settings
  generate_LLM_Response() {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }

    let httpBody = {
      "TitlePlain": this.input.product_info.TitlePlain,
      "DeliveryContents": this.input.product_info.DeliveryContents.split(',').map(el => el.trim()),
      "UserInstructions": this.input.product_info.UserInstructions.split(',').map(el => el.trim()),
      "UserCustomization": this.input.product_info.UserCustomization,

      "Title?": this.input.output_settings.Title,
      "DescriptionLong?": this.input.output_settings.DescriptionLong,
      "SalesArguments?": this.input.output_settings.SalesArguments,
      "BulletPoints?": this.input.output_settings.BulletPoints,
      "xxx?": this.input.output_settings.xxx
    }

    // push new user message to message array if the product id was selected in settings
    Object.entries(this.input.output_settings).forEach((entry) => {
      if(entry[1]) {
        this.product_info_array[this.product_info_array.findIndex((product_info) => product_info.product_id == entry[0])].message_array.push({
          llm_bot: false,
          timestamp: "23 Jan 2:00 pm",
          message: `Generiere ${entry[0]} für ${JSON.stringify(httpBody)}`
        })
      }
    })

    // create a dummy http request
    // for testing (dont need to send request to llm)
    if(this.dummy_http_request) {
      this.http.get<string[][]>('http://127.0.0.1:5000/status').pipe(delay(2000))
      .subscribe(response => {
        let dummy_response = [
          ["Title?", "\"Stilvolles Design: Einfache Montage und vielseitige Platzierungsm\u00f6glichkeiten f\u00fcr kompakte Gr\u00f6\u00dfe - Sicherheitshinweis f\u00fcr Kleinkinder und praktische Bedienungsanleitung. Hochwertiges Kabelmaterial, moderne Optik und inklusive Lampenk\u00f6rper f\u00fcr energiesparende Beleuchtung\""],
          ["SalesArguments?", "1. Stilvolles Design: Unsere Produkte verbinden \u00c4sthetik und Funktionalit\u00e4t, um Ihrem Zuhause einen Hauch von Eleganz zu verleihen.\n\n2. Einfache Montage: Mit unserer benutzerfreundlichen Montageanleitung k\u00f6nnen Sie Ihr Produkt ohne gro\u00dfen Aufwand schnell und einfach aufbauen.\n\n3. Vielseitige Platzierungsm\u00f6glichkeiten: Dank des kompakten Designs und der flexiblen Einsatzm\u00f6glichkeiten finden unsere Produkte in jedem Raum den perfekten Platz.\n\n4. Kompakte Gr\u00f6\u00dfe: Trotz seiner Leistungsf\u00e4higkeit ben\u00f6tigt unser Produkt nur wenig Platz und passt sich nahtlos in jeden Raum ein.\n\n5. Sicherheitshinweis f\u00fcr Kleinkinder: Wir legen besonderen Wert auf die Sicherheit Ihrer Familie und haben daher spezielle Sicherheitshinweise f\u00fcr den Gebrauch mit Kleinkindern integriert.\n\n6. Praktische Bedienungsanleitung: Unsere umfassende Bedienungsanleitung erleichtert Ihnen die Handhabung und sorgt f\u00fcr eine reibungslose Nutzung.\n\n7. Hochwertiges Kabelmaterial: Mit best\u00e4ndigen und hochwertigen Kabelmaterialien bieten wir Ihnen eine zuverl\u00e4ssige und langlebige Nutzung.\n\n8. Moderne Optik: Unsere Produkte sind nicht nur funktional, sondern \u00fcberzeugen auch mit einem zeitgem\u00e4\u00dfen und ansprechenden Design.\n\n9. Inklusive Lampenk\u00f6rper: Unser Produkt beinhaltet bereits einen hochwertigen Lampenk\u00f6rper, um Ihnen eine komplette L\u00f6sung zu bieten.\n\n10. Energiesparend: Mit unserem energieeffizienten Design sparen Sie nicht nur Energiekosten, sondern schonen auch die Umwelt."],
          ["BulletPoints?", "- Stilvolles Design\n- Einfache Montage\n- Vielseitige Platzierungsm\u00f6glichkeiten\n- Kompakte Gr\u00f6\u00dfe\n- Sicherheitshinweis f\u00fcr Kleinkinder\n- Praktische Bedienungsanleitung\n- Hochwertiges Kabelmaterial\n- Moderne Optik\n- Inklusive Lampenk\u00f6rper\n- Energiesparend"]
        ]
        
        dummy_response.forEach(llmResponse => {
          // only set dummy response if the product id was selected in settings
          let res_string = llmResponse[0].replace('?', '')
          if(res_string == "Title" || res_string == "SalesArguments" || res_string == "BulletPoints") {
            if(this.input.output_settings[res_string]) {
              // match product id of response to product_info_array and push response to message_array
              this.product_info_array[this.product_info_array.findIndex((product_info) => product_info.product_id == (llmResponse[0].replace('?', '')))].message_array.push({
                llm_bot: true,
                timestamp: "23 Jan 2:00 pm",
                message: llmResponse[1]
              })
            }
          }
        })
      })
    } else {
      // send request to backend and use actual llm
      this.http.post<string[][]>('http://127.0.0.1:5000/generate', JSON.stringify(httpBody), httpOptions)
      .subscribe(response => {
        response.forEach(llmResponse => {
          // match product id of response to product_info_array and push response to message_array
          this.product_info_array[this.product_info_array.findIndex((product_info) => product_info.product_id == (llmResponse[0].replace('?', '')))].message_array.push({
            llm_bot: true,
            timestamp: "23 Jan 2:00 pm",
            message: llmResponse[1]
          })
        })
      })
    }
  }

  copy_to_clipboard(str: string) {
    navigator.clipboard.writeText(str)
  }
}