# 1dev-hridoy/Clave-App

⭐ 14 · EJS · MIT · 推送 2026-06-23 · [GitHub](https://github.com/1dev-hridoy/Clave-App) · [官网](https://clave-app.onrender.com/) · 个人维护

**自托管 AI 聊天与图像生成 Web 应用，带 RESTful API**

基于 Node.js/Express/EJS/Tailwind CSS 的隐私优先 AI 界面：提供多模型聊天（GPT-4o、GPT-3.5 等）与图像生成（DeepImg、Flux），内置输入校验、XSS 防护、日志脱敏等安全特性，并暴露 /api/chat、/api/image 等 RESTful 端点。用户需自带 API key，通过 fork 克隆、npm install、npm start 在本地 3000 端口运行。面向想部署私有聊天界面或在其上二次开发的开发者，模型列表可通过 config/models.js 增删。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型聊天集成（GPT-4o、GPT-3.5 等）
- DeepImg 与 Flux 模型图像生成
- RESTful API（chat/image/status/reset）与应用内 /docs 文档
- 输入校验、XSS 防护、日志脱敏等内置安全特性

## 适用场景

- 部署一个自托管的私有 AI 聊天界面
- 以其为模板二次开发自定义 AI 工具
- 学习在 Node.js 中集成多个 AI 模型的方式

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L14: Welcome to **Clave App** - a sophisticated, privacy-focused AI interface designed for developers and enthusiasts wh
> L81: * `POST /api/chat` - Advanced chat completions with conversation history

## 星数曲线

```mermaid
xychart-beta
    title "1dev-hridoy/Clave-App 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `caf0888182ed` · [字段定义](../../DATASET.md)*
