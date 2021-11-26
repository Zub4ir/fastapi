FROM nginx:1.15.8

# inject custom config
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/