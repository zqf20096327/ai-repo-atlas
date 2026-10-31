# vitas/evidra

⭐ 15 · Go · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/vitas/evidra) · [官网](https://evidra.cc) · 个人维护

**MCP 执行证据记录器：留存代理声明/代理观察/汇报三方记录**

用 Go 编写的开源 MCP 执行证据记录代理：包在一个上游 stdio MCP 服务器之前，记录代理调用前的声明（declared）、代理边界观察到的执行起止/状态/指纹（observed）与代理收尾汇报（reported），形成本地签名、哈希链接的证据链，并由 CLI（summarize/verify）核对链完整性与签名。每端点进程仅支持一个上游服务器，不做沙箱，以调用者系统权限启动上游进程；不证明外部系统达到预期状态。当前为未发布的预览版，需 Go 1.26+ 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 声明/观察/汇报三方记录分离并以签名哈希链本地留存
- evidra summarize / verify CLI 核对链完整性与签名
- 支持 MCP 协议版本 2025-06-18 / 2025-03-26 / 2024-11-05
- 无需托管服务，本地证据目录运行

## 适用场景

- 审计 MCP agent 的工具调用过程与代理自述是否一致
- 为 agent 执行留存可验证的本地证据链
- 发现执行开始但无对应结束事件的未闭合操作

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Evidra is an open-source MCP execution-evidence recorder. It wraps one upstream
> L13: Agent / MCP client -> Evidra MCP endpoint -> upstream MCP server
> L97: - One stdio upstream MCP server per Evidra endpoint process.

## 星数曲线

```mermaid
xychart-beta
    title "vitas/evidra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ddd69af04c02` · [字段定义](../../DATASET.md)*
