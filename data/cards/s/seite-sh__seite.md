# seite-sh/seite

⭐ 26 · Rust · MIT · 推送 2026-10-28 · [GitHub](https://github.com/seite-sh/seite) · [官网](https://seite.sh) · 个人维护

**AI-native 静态网站生成器：Claude Code 作为内容管理界面**

用 Rust 编写的静态网站生成器，以单个二进制分发，无 JavaScript 运行时与构建依赖。核心机制：`seite agent` 调用用户已有的 Claude Code 订阅在完整站点上下文中写作内容；内置 MCP 服务器（stdio）向 Claude Code、Codex CLI、Cursor 等 MCP 兼容工具暴露站点资源与构建/搜索/修改工具；每次构建生成 llms.txt、llms-full.txt 与每页 .md 副本供 LLM 索引。功能含 10 个内置主题、6 种集合预设、多语言、图片管线、多站点工作区与部署向导。收集匿名可退出的使用遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `seite agent` 复用已有 Claude Code 订阅，无需额外 API key
- 内置 MCP 服务器暴露 13 个站点资源与工具，兼容多种 MCP 版本
- 每次构建生成 llms.txt / llms-full.txt 及每页 markdown 副本
- 单二进制覆盖构建/主题/多语言/部署，Rust 实现含 331 个测试

## 适用场景

- 用自然语言让 Claude Code 代写博客、文档与更新日志
- 让 MCP 兼容的 AI 工具以结构化接口读取和修改我的站点
- 构建同时面向浏览器 SEO 与 LLM 索引（GEO）的站点

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  A static site generator where Claude Code is the interface.

## 星数曲线

```mermaid
xychart-beta
    title "seite-sh/seite 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `20b3bd23130c` · [字段定义](../../DATASET.md)*
