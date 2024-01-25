import { Pipe, PipeTransform } from '@angular/core';
import { ProductInformation } from './app.component';

@Pipe({
  name: 'sortByOrder'
})
export class SortByOrderPipe implements PipeTransform {

  transform(object_array: {key: string, value: ProductInformation}[]): any[] {
    return object_array.sort((n1, n2) => {
      return n1.value.order - n2.value.order;
    });
  }
}
