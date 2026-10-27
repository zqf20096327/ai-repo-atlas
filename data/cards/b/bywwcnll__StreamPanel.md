# bywwcnll/StreamPanel

⭐ 185 · JavaScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/bywwcnll/StreamPanel) · 个人维护 · 中文 README

**Chrome DevTools 扩展：实时监控与检查 SSE/Fetch 流式请求**

以 Chrome DevTools 面板形式拦截并展示页面中的 EventSource、Fetch 流和 XMLHttpRequest 连接，开发者可实时查看消息、按 JSON 字段值过滤、全文搜索、按字段路径（如 choices.0.delta.content）聚焦显示，并以 JSON/CSV 导出、导入归档数据，支持 iframe 场景、连接持久化（IndexedDB）与统计。面向调试流式 API（含 ChatGPT、DeepSeek 等 AI 应用流式响应）的开发者与 QA。安装方式为 chrome://extensions 加载未打包扩展目录；二次开发需 Node.js v14+ 与 pnpm，用 Rollup 打包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拦截 EventSource、Fetch 流与 XMLHttpRequest 三类连接
- 消息按 JSON 字段值过滤（等于/包含、多条件 AND、嵌套与数组字段）
- JSON/CSV 导出与 JSON 会话导入，导出含连接元数据
- iframe 内流式连接监控与 IndexedDB 连接持久化

## 适用场景

- 调试 AI 聊天应用的流式响应内容
- 测试服务器发送事件与实时推送接口
- 对大量流式消息做字段过滤、搜索与导出分析

## 场景标签

 · 领域:开发者工具/浏览器扩展

## 证据(README 行号)

> L12: **Stream Panel** is a Chrome DevTools extension that allows developers to monitor and inspect streaming requests in
> L25: - ✅ Debugging AI chat application streaming responses

## 星数曲线

```mermaid
xychart-beta
    title "bywwcnll/StreamPanel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 184 --> 186
    line [185, 185]
```

2026-10-18 185 → 2026-10-27 185（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `1d110a064831` · [字段定义](../../DATASET.md)*
