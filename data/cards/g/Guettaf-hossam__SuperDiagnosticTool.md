# Guettaf-hossam/SuperDiagnosticTool

⭐ 19 · Python · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/Guettaf-hossam/SuperDiagnosticTool) · [官网](https://github.com/Guettaf-hossam/SuperDiagnosticTool/releases) · 个人维护

**Windows 系统诊断工具：Gemini 分析遥测并生成 PowerShell 修复脚本**

面向 Windows 10/11 的桌面诊断与修复工具：本地采集 CPU、内存、网络、安全、磁盘等系统遥测，将遥测快照发送到 Google Gemini API 分析，生成 PowerShell 修复脚本。脚本需通过四层验证（知识库匹配、干跑模拟、脚本校验、关键路径拦截）并经用户批准后在主机直接执行（非 VM/容器隔离）；执行前自动创建系统还原点并生成回滚脚本。提供免 Python 的独立 exe 与源码运行两种方式，需管理员权限与 Gemini API key，GPL v3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini API 分析系统遥测并生成 PowerShell 修复脚本
- 四层脚本验证管线与关键路径拦截（HKLM/HKCU、System32）
- 自动系统还原点、前后快照与回滚脚本生成
- 支持 1-128+ 核 CPU 的硬件适配与降级处理，生成 HTML 诊断报告

## 适用场景

- 描述系统问题后让 AI 生成并执行修复脚本
- 对 Windows 做快速/深度/完整三档系统体检并出 HTML 报告
- 排查性能异常、可疑进程与潜在恶意软件迹象

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: SuperDiagnosticTool collects real-time hardware telemetry, sends it to the Google Gemini API for analysis, and gene
> L28: - **Google Gemini Integration:** AI-powered system analysis and diagnostics via the Gemini API
> L211: - To generate AI recommendations, a telemetry snapshot (CPU load, memory, process names, event log entries, networ

## 星数曲线

```mermaid
xychart-beta
    title "Guettaf-hossam/SuperDiagnosticTool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `3ac9e5a07917` · [字段定义](../../DATASET.md)*
