FROM ruby:2.5.3

RUN apt-get update -qq && apt-get install -y nodejs

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN bundle install

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 3001

CMD ["rails", "server", "-b", "0.0.0.0"]
