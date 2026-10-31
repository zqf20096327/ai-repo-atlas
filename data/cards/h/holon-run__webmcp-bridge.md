# holon-run/webmcp-bridge

⭐ 28 · TypeScript · MIT · 推送 2026-04-12 · [GitHub](https://github.com/holon-run/webmcp-bridge) · [官网](https://webmcp-bridge.holon.run) · 组织维护

**把本地 MCP 客户端经 Playwright 接入浏览器 WebMCP 工具的桥接器**

通过 Playwright 驱动浏览器页面，将本地 stdio MCP 客户端的 tools/list 与 tools/call 代理到浏览器侧 WebMCP 执行：页面提供原生 WebMCP 时调用 navigator.modelContext，否则回退到注入的适配器路径，两者均返回标准 JSON MCP 载荷。面向 MCP 客户端作者、浏览器应用作者与适配器作者。每进程持有单个站点会话，复用已登录的浏览器会话而非迁移凭据；无原生 WebMCP 与适配器时进入 overlay-bootstrap 模式。限制：假定用户已在浏览器会话中完成认证，不做凭据保管或认证绕过。以 npm 包、npx 直接运行及 monorepo 源码方式提供，并附带六个 agent skills。

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

- 本地 stdio MCP → Playwright → navigator.modelContext 的统一调用路径
- 原生 WebMCP 缺失时回退到注入适配器（内置 x/weibo/fixture，支持外部适配器模块）
- 复用同一已登录浏览器会话，支持 headless 与可见窗口的人机协作模式
- 附带六个 agent skills 与适配器创作工作流（webmcp-adapter-creator）

## 适用场景

- 让本地 MCP 客户端调用网站上暴露的 WebMCP 工具
- 为尚无原生 WebMCP 的站点注入回退适配器
- 在同一可见浏览器会话中实现人与 AI 协作操作页面
- 为集成/契约测试使用确定性 fixture 适配器

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: `webmcp-bridge` lets a local MCP client call browser WebMCP tools through a stable local bridge.
> L26: `webmcp-bridge` keeps execution in the browser where those capabilities already exist, while exposing a normal loca
> L203: `webmcp-local-mcp` owns one site session per process, drives a Playwright page, and proxies `tools/list` / `tools/

## 星数曲线

```mermaid
xychart-beta
    title "holon-run/webmcp-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cc8db5a1d209` · [字段定义](../../DATASET.md)*
