import { Controller, Get, Param } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }

  @Get('getcode')
  getCode(): { code: string } {
    return { code: '12345' };
  }

  @Get('plus/:num1/:num2')
  plus(
    @Param('num1') num1: string,
    @Param('num2') num2: string,
  ): { result: number } {
    const result = this.appService.plus(parseFloat(num1), parseFloat(num2));
    return { result };
  }
}
