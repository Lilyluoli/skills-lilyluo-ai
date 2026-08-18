# Skill精选 / skills.lilyluo.ai

一个帮助你发现和上手 Agent Skills 的静态目录站。

## 这里是什么？

Skill 是可以被 AI Agent 调用的一组可复用能力。本项目从公开 Skill 生态中筛选高下载量、实用性较强的工具，并按开发、设计、内容、效率等场景整理，帮助你少一点搜索，多一点上手。

## 怎么使用？

1. 打开线上目录：[Skill精选](https://lilyluoli.github.io/skills-lilyluo-ai/)
2. 按分类筛选，或搜索你需要的任务与场景。
3. 阅读每张卡片的用途和推荐理由。
4. 点击卡片底部的“查看来源”，进入原作者页面，按照原页面说明安装或使用。

## 数据来源

- [skills.sh](https://skills.sh/)：Agent Skills 公开目录
- [SkillsMP](https://skillsmp.com/zh)：Skill 搜索与发现平台

## 本地运行

项目是零依赖静态站点，需要 Node.js 20 或更高版本：

```bash
npm run build
```

构建结果会写入 `dist/`，可直接部署到任意静态托管服务。

## GitHub Pages 部署

仓库已配置 `.github/workflows/pages.yml`。每次推送到 `main` 分支后，GitHub Actions 会自动构建并发布到：

<https://lilyluoli.github.io/skills-lilyluo-ai/>

每天运行的 `Update curated skills` 工作流会更新 `data/skills.json`。
