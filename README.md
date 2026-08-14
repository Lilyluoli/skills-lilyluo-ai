# Skill精选 / skills.lilyluo.ai

从 skillsmp.com/zh 与 skills.sh 精选高下载量 Agent Skills 的静态目录站。

## 部署

本项目是零依赖静态站点，可直接放到 Nginx、Caddy、Cloudflare Pages 或任意 VPS 静态目录。域名 `skills.lilyluo.ai` 在 DNS 中添加 A/AAAA 记录指向 VPS，再由 Nginx/Caddy 配置 HTTPS。

## 数据更新

首页数据目前位于 `index.html` 的 `skills` 数组，字段包括名称、作者、分类、下载量、介绍、推荐理由与标签。建议后续接入定时抓取，将生成结果写入 `data/skills.json`，前端改为 fetch 读取。

## GitHub 私库

在 GitHub 创建 Private repository 后：

```bash
git init && git add . && git commit -m "feat: launch skill精选"
git branch -M main && git remote add origin <PRIVATE_REPOSITORY_URL>
git push -u origin main
```
