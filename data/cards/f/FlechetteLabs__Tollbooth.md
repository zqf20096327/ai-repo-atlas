# FlechetteLabs/Tollbooth

⭐ 21 · TypeScript · AGPL-3.0 · 推送 2026-04-16 · [GitHub](https://github.com/FlechetteLabs/Tollbooth) · [官网](https://flechettelabs.com/Tollbooth/) · 组织维护

**面向 LLM 编码代理的透明流量审计代理：抓包/查看/改写请求**

基于 mitmproxy 的中间人透明代理，捕获代理容器内全部 HTTP/HTTPS 流量：LLM API 调用被解析为可读对话并展示为 gitflow 风格的对话树，其余流量按原始形式展示。支持在请求到达目的地前拦截修改、用存储响应模拟回复、基于优先级的规则引擎自动处理流量、导出对话为 JSON/Markdown/HTML，并以 ML 检测 LLM 拒答。兼容 Claude Code、Codex CLI、Cursor、Aider 等工具，文档声明仅供研究开发用途，流量会写入磁盘。可选集成 Glossopetrae 构造型语言解码引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM API 调用自动解析为对话并可视化分支/重试/合并树
- 拦截修改任意请求、模拟响应、优先级规则引擎
- 对话导出为 JSON/Markdown/HTML
- ML 检测 LLM 拒答并自动处理

## 适用场景

- 研究/调试 LLM 编码代理的网络行为与对话分支
- 对代理流量做安全测试与审计
- 通过规则引擎自动改写或拦截特定请求

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A transparent proxy for inspecting, debugging, and modifying network traffic—built for LLM agent research but applic
> L11: Tollbooth is a man-in-the-middle proxy that captures **all network traffic** from the agent container. While built 

## 星数曲线

```mermaid
xychart-beta
    title "FlechetteLabs/Tollbooth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b5f38d006000` · [字段定义](../../DATASET.md)*
