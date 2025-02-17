import { Test, TestingModule } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';

describe('AppController', () => {
  let appController: AppController;

  beforeEach(async () => {
    const app: TestingModule = await Test.createTestingModule({
      controllers: [AppController],
      providers: [AppService],
    }).compile();

    appController = app.get<AppController>(AppController);
  });

  describe('getcode', () => {
    it('should return code "12345"', () => {
      expect(appController.getCode()).toEqual({ code: '12345' });
    });
  });

  describe('plus', () => {
    it('should return sum of two numbers', () => {
      expect(appController.plus('5', '6')).toEqual({ result: 11 });
      expect(appController.plus('10', '20')).toEqual({ result: 30 });
    });
  });
});
