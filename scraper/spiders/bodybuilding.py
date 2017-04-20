import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BodyBuildingSpider(scrapy.Spider):

    name = 'bodybuilding' 
    start_urls = ['https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/1/muscle/chest']

    



    def __init__(self):
        self.driver = webdriver.Firefox()


    def parse(self, response):

        manual_urls = ['https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/6/muscle/neck',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/11/muscle/traps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/12/muscle/shoulders',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/15/muscle/biceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/2/muscle/forearms',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/13/muscle/abdominals',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/7/muscle/quadriceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/9/muscle/calves',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/10/muscle/triceps',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/3/muscle/lats',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/4/muscle/middle-back',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/5/muscle/lower-back',
                        'https://www.bodybuilding.com/exercises/finder/lookup/filter/muscle/id/14/muscle/glutes']

                        

        url_index = 0

        self.driver.get(response.url)
        time.sleep(10) # wait for page to load before hitting next
        exercises = response.css("div[class*=altExercise]")
                
        # grab first page
        for exercise in exercises:
                    
           yield  {
                    'exercise_name': exercise.css('div.exerciseName > h3 > a::text').extract_first(),
                    'target_muscle': exercise.css('div.exerciseName > p > span > a::text').extract_first(),
                    'exercise_rating': exercise.css('div.exerciseRating span.rating::text').extract_first(),
          }


        while True:

            has_next_page = len(self.driver.find_elements(By.CSS_SELECTOR, '.next > a:nth-child(1)')) > 0
            print("HAS NEXT PAGE = ", has_next_page)
            
            if has_next_page: 
                next_page = self.driver.find_element_by_css_selector('.next > a:nth-child(1)')
            else:
                if url_index < len(manual_urls):
                    yield scrapy.Request(manual_urls[url_index], callback=self.parse)
                    print('URL INDEX', url_index)
                    url_index += 1




            try:
                next_page.click()
                time.sleep(5)



                sel = Selector(text=self.driver.page_source)
                exercises = sel.css("div[class*=altExercise]")
                

                for exercise in exercises:
                    
                    yield  {
                        'exercise_name': exercise.css('div.exerciseName > h3 > a::text').extract_first(),
                        'target_muscle': exercise.css('div.exerciseName > p > span > a::text').extract_first(),
                        'exercise_rating': exercise.css('div.exerciseRating span.rating::text').extract_first(),
                    }
                    
                    

            except Exception as e:
                pass
                print('my Exception', e)




        self.driver.close()