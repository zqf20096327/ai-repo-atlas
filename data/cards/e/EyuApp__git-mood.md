# EyuApp/git-mood

⭐ 14 · JavaScript · 推送 2026-06-07 · [GitHub](https://github.com/EyuApp/git-mood) · [官网](https://www.npmjs.com/package/git-mood) · 个人维护

**用 Gemini 生成 Conventional 提交信息与代码审查的 Git CLI 助手**

基于 Node.js 的命令行 Git 助手，调用 Google Gemini Flash 系列模型（2.5 Flash-Lite、2.5 Flash、Flash 3）完成三项 AI 任务：分析暂存 diff 生成 Conventional Commits 格式提交信息并可提交/推送；对未暂存与暂存改动做代码审查，识别逻辑错误与暴露的密钥；生成项目 README。API key 通过 setup 命令本地存储（conf 包），diff 直连 Gemini API 不经中间服务。需要 Node.js v18+ 与已初始化的 Git 环境，通过 npm 全局安装或 npx 直接运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分析暂存 diff 生成 Conventional Commits 提交信息
- 对 diff 做 AI 代码审查（逻辑错误、暴露密钥）
- AI README 生成器
- 支持 Gemini 2.5 Flash-Lite / Flash 2.5 / Flash 3 模型切换

## 适用场景

- 写提交信息时让 AI 根据 diff 自动生成规范化消息
- 推送前对改动做快速代码审查
- 为新项目自动生成 README

## 场景标签

`代码审查` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L6:  Generate conventional commits, perform deep code reviews, and push to GitHub—all with Google Gemini.
> L25: Powered by the latest **Gemini Flash** models (Lite 2.5, 2.5, and 3).

## 星数曲线

```mermaid
xychart-beta
    title "EyuApp/git-mood 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `69ba5ad886ad` · [字段定义](../../DATASET.md)*
