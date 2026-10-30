# andreinwald/webmcp-demo

⭐ 15 · TypeScript · 推送 2026-06-09 · [GitHub](https://github.com/andreinwald/webmcp-demo) · [官网](https://andreinwald.github.io/webmcp-demo) · 个人维护

**鞋店 WebMCP 演示站点：在网页内注册 MCP 工具供浏览器调用**

面向 Google Chrome（149+ 且开启 WebMCP flag）的演示项目：以一个鞋店网页为载体，展示 WebMCP 规范的用法——通过 DevTools 的 Inspect > Application > WebMCP 面板调用站点注册的工具（如按品牌筛选、加购物车、完成购买）。代码侧提供 registerMCP 辅助函数，用 Zod 生成 JSON Schema 并校验 LLM 输入，另有 React 的 useRegisterMCP 封装；更多示例见 DemoStore.tsx。属于标准草案阶段的功能演示，依赖实验性浏览器开关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在网页内注册 MCP 工具（filter_by_brand、add_to_cart 等）
- registerMCP 用 Zod 生成 inputSchema JSON Schema 并校验输入
- 提供 React useRegisterMCP 封装
- 需 Chrome 149+ 并在 chrome://flags 启用 WebMCP for testing

## 适用场景

- 体验和学习 WebMCP 规范在真实网页中的用法
- 参考 registerMCP/useRegisterMCP 编写自己的 WebMCP 站点
- 通过 DevTools WebMCP 面板测试站点工具调用

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: WebMCP requires an "instance" of website that has JavaScript runtime and likely a DOM tree. In other words, the brow
> L9: - Go to chrome://flags and enable "WebMCP for testing"
> L19: This repo has helper function registerMCP that allows you build ZOD schema which way easier and also doin validatio

## 星数曲线

```mermaid
xychart-beta
    title "andreinwald/webmcp-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `346e708a8c1e` · [字段定义](../../DATASET.md)*
