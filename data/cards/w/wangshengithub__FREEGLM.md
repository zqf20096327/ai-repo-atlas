# wangshengithub/FREEGLM

⭐ 23 · HTML · MIT · 推送 2026-06-06 · [GitHub](https://github.com/wangshengithub/FREEGLM) · 个人维护 · 中文 README

**免配置的 GLM-4 网页对话客户端，本地 Node.js 代理转发请求**

基于 HTML/CSS/JS 前端与 Node.js + Express 本地代理服务器的 GLM-4 AI 对话工具。代理自动修改 Origin/Referer 请求头并通过 Cookie 维持会话，绕过官方 API 跨域限制，前端经 SSE 接收流式响应，支持上下文记忆。使用 git clone 克隆后 npm install、npm start，浏览器访问 localhost:33333 即可。请求转发至第三方 API（v8.qqslyx.com），作者声明非官方产品，提示勿输入隐私数据，且依赖上游服务可用性。

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

- 内置本地 Node.js 代理修改 Origin/Referer 头以绕过 CORS
- SSE 流式响应与上下文记忆
- 克隆后 npm install / npm start 即可运行，无需配置

## 适用场景

- 在本地免费进行 GLM-4 对话
- 不想安装浏览器插件直接使用网页聊天界面

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: FREEGLM 是一个基于 GLM-4 的免费 AI 对话工具，无需任何配置即可在本地运行。
> L29: * 🚀 **开箱即用**：内置代理，解决了官方 API 的跨域限制，无需安装浏览器插件。
> L71: * 自动修改请求头 `Origin` 和 `Referer` 以通过 API 验证。

## 星数曲线

```mermaid
xychart-beta
    title "wangshengithub/FREEGLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d67bbf2343fb` · [字段定义](../../DATASET.md)*
