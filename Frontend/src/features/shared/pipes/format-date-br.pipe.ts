import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'formatDateBr',
  standalone: true
})
export class FormatDateBrPipe implements PipeTransform {

  transform(value: string | Date): string {
    if (!value) {
      return '';
    }

    let date: Date;

    if (typeof value === 'string') {
      date = new Date(value.replace(/-/g, '/').replace('T', ' ').split('.')[0]);
    } else {
      date = new Date(value);
    }

    if (isNaN(date.getTime())) {
      return 'Invalid Date';
    }

    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();

    return `${day}/${month}/${year}`;
  }
}
