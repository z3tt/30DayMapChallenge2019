library(dplyr)
library(stringr)
library(ggplot2)
library(forcats)
library(textreadr)

geoms <- read_dir(path = here::here(), pattern = "\\.R", recursive = TRUE) %>% 
  mutate(geom = str_extract(content, "geom_\\w+")) %>%  # assumes one geom per line
  filter(!is.na(geom)) %>% 
  count(geom) %>% 
  mutate(
    freq = n / sum(n),
    total_geoms = sum(n),
    geom = fct_reorder(geom, n)
  )  %>% 
  arrange(-n)

top_20 <- geoms %>%
  slice_max(n, n = 20)

c1 = "grey95" # background
c2 = "grey20" 

ggplot(top_20) +
  geom_col(aes(n, geom), width = 0.6, fill = c2) +
  geom_text(aes(n + 1, geom, label = n), size = 3 , hjust = 0, family = "Fira Code", color = c2) +
  theme_minimal(base_family = "Fira Sans") +
  theme(
    axis.title = element_blank(),
    axis.text = element_text(color = c2, family = "Fira Code"),
    plot.title = element_text(color = c2, hjust = 0, size = 18, face = "bold"), 
    plot.title.position = "plot",
    panel.grid.major.y = element_blank(),
    plot.background = element_rect(fill = c1, color = NA),
    plot.margin = margin(rep(20, 4))
  ) + 
  scale_x_continuous(expand = c(.001, .001), limits = c(0, 155)) +
  labs(title = "geom's used in 28 contributions to 30DayMapChallenge 2019") +
  ggsave("maps_geom.pdf", width = 10, height = 4, device = cairo_pdf)
