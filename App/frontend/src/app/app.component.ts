import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { delay } from 'rxjs/operators';
import { NgbNavModule } from '@ng-bootstrap/ng-bootstrap';

type MessageArray = { llm_bot: boolean, timestamp: string, message: string, prompt?: string }[]
type HTTP_LLM_Response = { typ: string, prompt: string, response: string }
export interface ProductInformation { select_for_generate: boolean, display_name: string, order: number, message_array: MessageArray, repromt_chat: string }

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private http: HttpClient) { }

  active = "TitleAmazon"
  dummy_http_request = true

  // input settings
  input = {
    product_info: {
      "TitlePlain": "",
      "DeliveryContents": "",
      "UserInstructions": "",
      "UserCustomization": ""
    },
    llm_settings: {
      "select_llm": "ChatGPT-3.5/Llama-selbstrainiert",
      "temperature": 0.5,
      "max_tokens": 2048,
      "top_p": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
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
  product_info_dict: { [product_id: string]: ProductInformation } = {
    "TitleAmazon": {display_name: "Titel", select_for_generate: false, order: 0, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" },
    "DescriptionLongShops": {display_name: "Produktbeschreibung", select_for_generate: false, order: 1, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" },
    "SalesArgument": {display_name: "Verkaufsargumente", select_for_generate: false, order: 2, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" },
    "AmazonBulletPoints": {display_name: "Bulletpoints", select_for_generate: false, order: 3, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" },
    "WorthKnowingShop": {display_name: "Worth Knowing", select_for_generate: false, order: 4, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" },
    "MetaKeywordShop": {display_name: "Meta Keywords", select_for_generate: false, order: 5, message_array: this.direct_chat_messages_array.map(object => ({ ...object })), repromt_chat: "" }
  }

  // function to set the standard for input settings
  set_std_input() {
    this.input = {
      product_info: {
        "TitlePlain": "Wandlampe",
        "DeliveryContents": "Lampenkörper",
        "UserInstructions": "10cm x 30cm",
        "UserCustomization": "Besonders freundlicher Output"
      },
      llm_settings: {
        "select_llm": "ChatGPT-3.5/Llama-selbstrainiert",
        "temperature": 0.5,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
      }
    }
    this.product_info_dict["TitleAmazon"].select_for_generate = true
    this.product_info_dict["DescriptionLongShops"].select_for_generate = true
    this.product_info_dict["SalesArgument"].select_for_generate = true
    this.product_info_dict["AmazonBulletPoints"].select_for_generate = true
    this.product_info_dict["WorthKnowingShop"].select_for_generate = true
    this.product_info_dict["MetaKeywordShop"].select_for_generate = true
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
      llm_settings: {
        "select_llm": "ChatGPT-3.5/Llama-selbstrainiert",
        "temperature": 0.5,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
      }
    }
    this.product_info_dict["TitleAmazon"].select_for_generate = false
    this.product_info_dict["DescriptionLongShops"].select_for_generate = false
    this.product_info_dict["SalesArgument"].select_for_generate = false
    this.product_info_dict["AmazonBulletPoints"].select_for_generate = false
    this.product_info_dict["WorthKnowingShop"].select_for_generate = false
    this.product_info_dict["MetaKeywordShop"].select_for_generate = false
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
      "product_information": {
        "TitlePlain": this.input.product_info.TitlePlain,
        "DeliveryContents": this.input.product_info.DeliveryContents.split(',').map(el => el.trim()),
        "UserInstructions": this.input.product_info.UserInstructions.split(',').map(el => el.trim()),
        "UserCustomization": this.input.product_info.UserCustomization
      },
      "generate_selection": {
        "TitleAmazon": this.product_info_dict["TitleAmazon"].select_for_generate,
        "DescriptionLongShops": this.product_info_dict["DescriptionLongShops"].select_for_generate,
        "SalesArgument": this.product_info_dict["SalesArgument"].select_for_generate,
        "AmazonBulletPoints": this.product_info_dict["AmazonBulletPoints"].select_for_generate,
        "WorthKnowingShop" : this.product_info_dict["WorthKnowingShop"].select_for_generate,
        "MetaKeywordShop" : this.product_info_dict["MetaKeywordShop"].select_for_generate
      },
      "llm_settings": {
        "select_llm": this.input.llm_settings.select_llm,
        "temperature": this.input.llm_settings.temperature,
        "max_tokens": this.input.llm_settings.max_tokens,
        "top_p": this.input.llm_settings.top_p,
        "frequency_penalty": this.input.llm_settings.frequency_penalty,
        "presence_penalty": this.input.llm_settings.presence_penalty
      }
    }

    // push new user message to message array if the product id was selected in settings
    for (const [key, value] of Object.entries(this.product_info_dict)) {
      if(value.select_for_generate) {
        this.product_info_dict[key].message_array.push({
          llm_bot: false,
          timestamp: "23 Jan 2:00 pm",
          message: `Generiere ${value.display_name} für die oben definierten Produktdaten.`
        })
      }
    }

    // create a dummy http request
    // for testing (dont need to send request to llm)
    if(this.dummy_http_request) {
      this.http.get<string[][]>('http://127.0.0.1:5000/status').pipe(delay(2000))
      .subscribe(response => {
        let dummy_response: HTTP_LLM_Response[] = [
          {typ: "TitleAmazon", prompt: "Testprompt...", response: "\"Stilvolles Design: Einfache Montage und vielseitige Platzierungsm\u00f6glichkeiten f\u00fcr kompakte Gr\u00f6\u00dfe - Sicherheitshinweis f\u00fcr Kleinkinder und praktische Bedienungsanleitung. Hochwertiges Kabelmaterial, moderne Optik und inklusive Lampenk\u00f6rper f\u00fcr energiesparende Beleuchtung\""},
          {typ: "DescriptionLongShops", prompt: "Testprompt...", response: "Entdecke unsere vielseitigen Aufbewahrungslösungen für ein organisiertes Zuhause! Unser elegantes Eckregal aus Metall bietet dir wertvollen Stauraum und hilft, Ordnung in deine Küche zu bringen. Mit einem hohen Rand, der ein Herausfallen der Lebensmittel verhindert, eignet sich das Regal ideal zur Aufbewahrung von Gewürzen und zum Einhängen von Kochgeschirr. Die kompakte Größe passt in jede Ecke und die unkomplizierte Montage mit den mitgelieferten großen Klebepads ermöglicht eine schnelle Befestigung ohne Bohren. \n\nVerleihe deinem Zuhause mit unserem cremefarbenen Makramee-Wandbehang aus Baumwolle eine gemütliche Atmosphäre. Die handgeknüpfte, traditionelle Knüpftechnik und das symmetrische Design schaffen ein behagliches Ambiente und setzen stilvolle Akzente in jedem Raum. Ob im Boho, Indie- oder Ibiza-Style – dieses Wandmakramee ist ein echter Hingucker.\n\nUnser dekorativer Allzweckkorb aus robustem und weichem Kunststoff ist die perfekte Lösung zur Aufbewahrung von Spielsachen, Kleidungsstücken und anderen Utensilien des täglichen Gebrauchs. Die Flechtoptik fügt sich harmonisch in jeden Raum ein und der faltbare Aufbewahrungskorb lässt sich bei Bedarf platzsparend zusammenfalten. Dank seiner pflegeleichten Eigenschaften ist er zudem schnell und einfach zu reinigen. Entdecke jetzt die vielseitigen Anwendungsmöglichkeiten dieses praktischen Allzweckkorbs!"},
          {typ: "SalesArgument", prompt: "Testprompt...", response: "1. Stilvolles Design: Unsere Produkte verbinden \u00c4sthetik und Funktionalit\u00e4t, um Ihrem Zuhause einen Hauch von Eleganz zu verleihen.\n\n2. Einfache Montage: Mit unserer benutzerfreundlichen Montageanleitung k\u00f6nnen Sie Ihr Produkt ohne gro\u00dfen Aufwand schnell und einfach aufbauen.\n\n3. Vielseitige Platzierungsm\u00f6glichkeiten: Dank des kompakten Designs und der flexiblen Einsatzm\u00f6glichkeiten finden unsere Produkte in jedem Raum den perfekten Platz.\n\n4. Kompakte Gr\u00f6\u00dfe: Trotz seiner Leistungsf\u00e4higkeit ben\u00f6tigt unser Produkt nur wenig Platz und passt sich nahtlos in jeden Raum ein.\n\n5. Sicherheitshinweis f\u00fcr Kleinkinder: Wir legen besonderen Wert auf die Sicherheit Ihrer Familie und haben daher spezielle Sicherheitshinweise f\u00fcr den Gebrauch mit Kleinkindern integriert.\n\n6. Praktische Bedienungsanleitung: Unsere umfassende Bedienungsanleitung erleichtert Ihnen die Handhabung und sorgt f\u00fcr eine reibungslose Nutzung.\n\n7. Hochwertiges Kabelmaterial: Mit best\u00e4ndigen und hochwertigen Kabelmaterialien bieten wir Ihnen eine zuverl\u00e4ssige und langlebige Nutzung.\n\n8. Moderne Optik: Unsere Produkte sind nicht nur funktional, sondern \u00fcberzeugen auch mit einem zeitgem\u00e4\u00dfen und ansprechenden Design.\n\n9. Inklusive Lampenk\u00f6rper: Unser Produkt beinhaltet bereits einen hochwertigen Lampenk\u00f6rper, um Ihnen eine komplette L\u00f6sung zu bieten.\n\n10. Energiesparend: Mit unserem energieeffizienten Design sparen Sie nicht nur Energiekosten, sondern schonen auch die Umwelt."},
          {typ: "AmazonBulletPoints", prompt: "Testprompt...", response: "- Stilvolles Design\n- Einfache Montage\n- Vielseitige Platzierungsm\u00f6glichkeiten\n- Kompakte Gr\u00f6\u00dfe\n- Sicherheitshinweis f\u00fcr Kleinkinder\n- Praktische Bedienungsanleitung\n- Hochwertiges Kabelmaterial\n- Moderne Optik\n- Inklusive Lampenk\u00f6rper\n- Energiesparend"},
          {typ: "WorthKnowingShop", prompt: "Testprompt...", response: "<h2>Nostalgische Wandgarderobe mit 5 Haken</h2>\n<ul>\n  <li><strong>Elegantes Design:</strong> Die nostalgische Wandgarderobe mit 5 Haken verleiht Ihrem Eingangsbereich oder Ihrer Küche einen antiken, barocken Look und dient gleichzeitig als originelles Dekoelement.</li>\n  <li><strong>Viel Stauraum:</strong> Schaffen Sie im Handumdrehen Platz für leichte Jacken, Schals, Schlüssel oder Geschirrtücher und halten Sie Ihren Raum ordentlich und organisiert.</li>\n  <li><strong>Einfache Montage:</strong> Die Hakenleiste lässt sich unkompliziert und schnell anbringen, sodass Sie sofort von den praktischen Vorteilen profitieren können.</li>\n  <li><strong>Vielseitige Anwendungsmöglichkeiten:</strong> Die kompakte Größe und die stilvoll eingearbeiteten Ornamente machen die Hakenleiste flexibel einsetzbar, sei es im Flur, in der Küche oder im Schlafzimmer.</li>\n  <li><strong>Positive Atmosphäre:</strong> Die nostalgische Wandgarderobe schafft eine gemütliche und einladende Atmosphäre in Ihrem Zuhause und sorgt für ein nostalgisches Flair.</li>\n</ul>"},
          {typ: "MetaKeywordShop", prompt: "Testprompt...", response: "Elegantes Design, modernes Design, einfache Montage, unkomplizierte Montage, flexibles Kabel, individuelle Platzierung, kompakte Größe, vielseitige Anwendungsmöglichkeiten, Sicherheitsmerkmal, Nicht für Kleinkinder geeignet"}
        ]
        
        dummy_response.forEach(llmResponse => {
          if(this.product_info_dict[llmResponse.typ].select_for_generate) {
            // match product id of response to product_info_array and push response to message_array
            this.product_info_dict[llmResponse.typ].message_array.push({
              llm_bot: true,
              timestamp: "23 Jan 2:00 pm",
              message: llmResponse.response,
              prompt: llmResponse.prompt
            })
          }
        })
      })
    } else {
      // send request to backend and use actual llm
      this.http.post<HTTP_LLM_Response[]>('http://127.0.0.1:5000/generate', JSON.stringify(httpBody), httpOptions)
      .subscribe(response => {
        response.forEach(llmResponse => {
          // match product typ of response to product_info_array and push response to message_array
          this.product_info_dict[llmResponse.typ].message_array.push({
            llm_bot: true,
            timestamp: "23 Jan 2:00 pm",
            message: llmResponse.response,
            prompt: llmResponse.prompt
          })
        })
      })
    }
  }


  reprompt(typ: string, prompt_original: string, prompt_response: string, instruction: string) {
    //check if any argument is undefined
    if(typ == undefined || prompt_original == undefined || prompt_response == undefined || instruction == undefined) {
      console.log("Error: undefined arguments")
      console.log(arguments)      
      
      return
    }
    
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    }

    let httpBody = {
      "typ": typ,
      "prompt_original": prompt_original,
      "prompt_response": prompt_response,
      "instruction": instruction,
      "llm_settings": {
        "select_llm": this.input.llm_settings.select_llm,
        "temperature": this.input.llm_settings.temperature,
        "max_tokens": this.input.llm_settings.max_tokens,
        "top_p": this.input.llm_settings.top_p,
        "frequency_penalty": this.input.llm_settings.frequency_penalty,
        "presence_penalty": this.input.llm_settings.presence_penalty
      }
    }

    // push new user message to message array containing the instruction
    this.product_info_dict[typ].message_array.push({
      llm_bot: false,
      timestamp: "23 Jan 2:00 pm",
      message: `Verbessere den vorherigen Prompt mittels der Anweisung: "${instruction}"`
    })

    // send request to backend and use actual llm
    this.http.post<HTTP_LLM_Response>('http://127.0.0.1:5000/reprompt', JSON.stringify(httpBody), httpOptions)
    .subscribe(llmResponse => {
      // push response to message_array
      this.product_info_dict[llmResponse.typ].message_array.push({
        llm_bot: true,
        timestamp: "23 Jan 2:00 pm",
        message: llmResponse.response,
        prompt: llmResponse.prompt
      })

      // reset repromt_chat message input
      this.product_info_dict[typ].repromt_chat = ""
    })
  }

  copy_to_clipboard(str: string) {
    navigator.clipboard.writeText(str)
  }
}