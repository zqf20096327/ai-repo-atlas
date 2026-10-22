# VictoriaMetrics/mcp-victoriametrics

⭐ 239 · Go · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/VictoriaMetrics/mcp-victoriametrics) · [官网](https://victoriametrics.com/) · 组织维护

**VictoriaMetrics 官方 MCP 服务器：让 AI 客户端查询监控数据**

由 VictoriaMetrics 团队实现的 Model Context Protocol 服务器，把 VictoriaMetrics 与 VictoriaMetrics Cloud 的几乎全部只读 API（VMUI 可用功能）以工具形式暴露给 MCP 客户端：指标查询与导出、告警/记录规则分析、基数探索、查询解释与调试、relabeling/降采样/保留策略调试等；内嵌离线可搜索文档。支持 stdio/SSE/Streamable HTTP 三种模式，通过环境变量配置实例地址与认证；提供二进制、Docker、源码构建与 Helm chart 四种安装方式，并给出 Cursor、Claude Desktop、Claude Code、Codex、VS Code、Zed、JetBrains、Windsurf 等客户端的接入配置。另有公开 Playground 实例可免安装试用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 暴露 VictoriaMetrics 几乎全部只读 API（查询/导出/告警分析/基数探索）
- 内嵌最新文档，支持离线搜索
- 支持 stdio/SSE/Streamable HTTP 三种传输模式
- 提供公开 Playground 实例免安装试用

## 适用场景

- 在 IDE 或 AI 客户端中用自然语言查询和调试 VictoriaMetrics 指标
- 让 AI 分析告警规则、relabeling 与保留策略配置
- 为运维排障场景接入可观测性数据源

## 场景标签

 · 领域:监控/可观测性基础设施

## 证据(README 行号)

> L10: The implementation of Model Context Protocol (MCP) server for VictoriaMetrics.
> L17: This MCP server allows you to use almost all read-only APIs of VictoriaMetrics, i.e. all functions available in VMU

## 星数曲线

```mermaid
xychart-beta
    title "VictoriaMetrics/mcp-victoriametrics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 237 --> 240
    line [238, 239]
```

2026-10-18 238 → 2026-10-22 239（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `78b129baaf1a` · [字段定义](../../DATASET.md)*
