# ty0x2333/ComfyUI-Dev-Utils

⭐ 197 · JavaScript · MIT · 推送 2025-11-01 · [GitHub](https://github.com/ty0x2333/ComfyUI-Dev-Utils) · 个人维护

**ComfyUI 开发者辅助工具集：执行耗时分析、Python 日志面板等**

面向 ComfyUI 开发者的自定义节点集合，提供节点执行耗时分析与表格展示（含前后执行对比与缓存清理按钮）、基于 SSE 的 Python 日志控制台（捕获 print/logging/stdout/stderr，可禁用）、Reroute 节点菜单增强与删除优化，以及 UrlDownload 与 UploadAnything 两个文件路径工具。通过 ComfyUI-Manager 安装或手动 git clone 至 custom_nodes 并 pip 安装依赖后重启 ComfyUI 使用。MIT 许可。

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

- 节点执行耗时 Badge 与执行时间表格（含前后差异对比）
- 基于 SSE 的 LogConsole 捕获 Python 日志输出并按颜色区分错误
- Reroute 菜单选项增强与 Reroute 节点删除优化
- UrlDownload / UploadAnything 文件路径工具节点

## 适用场景

- 排查 ComfyUI 工作流中各节点的执行耗时
- 在网页端查看 ComfyUI 后端 Python 日志
- 简化 Reroute 节点的添加与删除操作

## 场景标签

 · 领域:AI 工作流工具/开发者插件

## 证据(README 行号)

> L1: ComfyUI-Dev-Utils
> L25: 1. Execution Time Analysis Tool
> L49:  Provide a Console panel to display **Python logs** (**not** Javascript console.log).

## 星数曲线

```mermaid
xychart-beta
    title "ty0x2333/ComfyUI-Dev-Utils 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-23 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `d9b4ad1ff68a` · [字段定义](../../DATASET.md)*
