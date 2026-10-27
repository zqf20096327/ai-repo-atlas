# banggx/morgana-form

⭐ 147 · TypeScript · Apache-2.0 · 推送 2026-06-21 · [GitHub](https://github.com/banggx/morgana-form) · [官网](http://morgana-form.mxchensir.com/) · 个人维护 · 中文 README

**低代码问卷表单搭建器，支持 AI 生成表单与数据统计**

基于 Next 14 全栈开发的问卷表单搭建项目：提供低代码表单编辑器、表单数据收集与统计图表，集成 AI 表单生成能力（默认调用阿里千问大模型，可在 server/routes/llm.ts 中切换模型，也可移除相关代码）。技术栈含 React 18、Ant Design 5、PostgreSQL、Drizzle ORM、TRPC、NextAuth 登录与 Uppy 文件上传（默认七牛云存储）。需配置数据库、OAuth、存储与 LLM 等环境变量后运行。作者声明为第一版开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 低代码问卷表单编辑与数据收集统计（Ant Design Charts）
- AI 表单生成：默认千问大模型，支持自行切换或移除
- NextAuth 登录认证与 Uppy 文件上传（七牛云/S3 兼容存储）

## 适用场景

- 快速搭建问卷收集与统计项目
- 用 AI 生成表单题目结构
- 作为 Next 全栈开发的学习参考项目

## 场景标签

 · 领域:表单/低代码

## 证据(README 行号)

> L5: 最近研究Next全栈开发，做一个全栈问卷星表单搭建器项目，能够帮助快速搭建一个问卷表单收集项目，项目采用Next全栈开发，涉及技术栈如下:
> L71: > 项目采用了阿里千问大模型进行表单生成，可以尝试将大模型自行切换，调整 server/routes/llm.ts 文件中的调用逻辑即可。如果不需要AI能力，去除项目中的相关代码即可。

## 星数曲线

```mermaid
xychart-beta
    title "banggx/morgana-form 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-27 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `253687467554` · [字段定义](../../DATASET.md)*
