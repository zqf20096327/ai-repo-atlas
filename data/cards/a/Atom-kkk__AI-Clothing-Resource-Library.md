# Atom-kkk/AI-Clothing-Resource-Library

⭐ 29 · HTML · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Atom-kkk/AI-Clothing-Resource-Library) · [官网](https://ai-clothing-library.app.workbuddy.host/?sharecode=E2QQTAQUAL) · 个人维护 · 中文 README

**1407 张 AI 服装参考图的纯静态图库，支持上传与 AI 提示词生成**

单文件 HTML 静态图库：内联 1407 张 AI 生成服装参考图数据，本地 assets 目录存缩略图与展示图，断网可用。支持拖拽上传自有图片（存浏览器 IndexedDB/localStorage）、自定义分类与编号续号、中英文关键词搜索。AI 部分为需自备 API Key 的 DeepSeek 调用，按图片分类与关键词生成 60–90 词英文文生图提示词，模板可改写。图片著作权归原作者，禁止再分发图片数据本身。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零依赖单文件 HTML，双击 index.html 即可离线运行
- 上传图片存 IndexedDB，降级 localStorage，不上传服务器
- 调用 DeepSeek 生成英文文生图提示词，可改可存
- 提供从源站拉取 1407 张 PNG 原图的幂等脚本与三层校验

## 适用场景

- AI 绘画时查阅服装参考并生成文生图提示词
- 把自己收集的服装图上传归类、离线管理
- 部署到 GitHub Pages 或 NAS 做私人素材库

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L16: 原始图库是一套面向 AI 绘画的服装参考素材（不含任何人物），元数据为日文，单页静态 HTML。本项目在它的基础上做成一个**可以长期自己用下去**的工具：
> L21: 4. **能直接产出提示词** —— 点开任意一张图，点「生成」即调用 DeepSeek 写一条文生图英文提示词，可改、可复制、自动保存。


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `80cce0fb37d5` · [字段定义](../../DATASET.md)*
