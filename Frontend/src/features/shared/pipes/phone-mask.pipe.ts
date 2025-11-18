import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'phoneMask',
  standalone: true
})
export class PhoneMaskPipe implements PipeTransform {
  transform(value: string): string {
    if (!value) return value;
    const cleanedValue = value.replace(/\D/g, '');
    if (cleanedValue.length === 11) {
      return `(${cleanedValue.slice(0, 2)}) ${cleanedValue.slice(2, 3)} ${cleanedValue.slice(3, 7)}-${cleanedValue.slice(7, 11)}`;
    } else if (cleanedValue.length === 10) {
      return `(${cleanedValue.slice(0, 2)}) ${cleanedValue.slice(2, 6)}-${cleanedValue.slice(6, 10)}`;
    }

    return value;
  }
}