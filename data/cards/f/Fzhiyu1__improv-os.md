# Fzhiyu1/improv-os

⭐ 125 · JavaScript · MIT · 推送 2026-06-18 · [GitHub](https://github.com/Fzhiyu1/improv-os) · [官网](https://os.fzhiyu.dev) · 个人维护 · 中文 README

**每个应用都由 AI 现场生成的 macOS 风格网页 OS**

一个网页"操作系统"体验项目：桌面、菜单栏、Dock、窗口管理、Spotlight 为手写代码，系统内不预装任何应用——点开 Dock 或搜索即由 AI 实时生成（快轨 2-3 秒流式直出 HTML；慢轨为 opencode agent loop 写文件自检迭代），每次生成结果不同，可对缓存应用做增量修改。生成物跑在 sandbox iframe，API key 仅存服务端，os.http 带 SSRF 过滤。面向普通用户的在线体验，也支持自部署（Node ≥ 18，零 npm 依赖，Anthropic /v1/messages 兼容端点）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 快轨流式直出（2-3s）与慢轨 agent loop（16-27s）双轨生成
- 能力桥 os.ai/os.http/os.store/os.compute 让生成应用调用真实数据
- 搜索无缓存应用现编、落盘缓存、可要求改版重生成
- 安全设计：服务端持 key、sandbox iframe、SSRF 过滤、限流与日熔断

## 适用场景

- 在线体验 AI 现场编写应用的过程（免登录网页）
- 自部署一个应用全由 AI 生成的网页 OS
- 观察 agent loop 写文件、自检、迭代的真人秀过程

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: ImprovOS — a web "operating system" where every app is improvised by AI, live, the moment you open it.
> L15: 一个发到互联网上博大家一笑的体验项目：macOS 风格的网页"操作系统"。桌面、菜单栏、Dock、窗口管理、Spotlight 是手写的真代码——除此之外，**系统里没有任何应用**。

## 星数曲线

```mermaid
xychart-beta
    title "Fzhiyu1/improv-os 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 123 --> 126
    line [124, 125, 125]
```

2026-10-18 124 → 2026-10-26 125（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f0239640fcdf` · [字段定义](../../DATASET.md)*
