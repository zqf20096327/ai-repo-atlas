# ggvfx/film-breakdown-assistant

⭐ 10 · Python · MIT · 推送 2026-04-05 · [GitHub](https://github.com/ggvfx/film-breakdown-assistant) · 个人维护

**本地 LLM 解析电影剧本自动生成拍摄分解表**

面向副导演与制片经理的 Python 桌面工具（PySide6 GUI，Beta 阶段），通过 Ollama 本地运行 LLM，从剧本（PDF/FDX/DOCX/RTF）中提取场景、部门元素及安全风险标记。核心为 7 遍多 Agent 流水线：Harvester 提取、Continuity Agent 做实体对齐与状态跟踪、Review Flag Agent 生成 AD Alerts。支持暂停/续跑的 JSON 检查点，输出 Excel/CSV，规划中的 .sex 格式用于 Movie Magic Scheduling。所有处理离线进行，敏感 IP 不出本机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 7-Pass 多 Agent 流水线：提取、连续性对齐、安全风险扫描
- 本地 Ollama 离线推理，支持 GPU 加速与模型热切换
- 15+ 部门元素提取与可切换的保守/推断模式
- JSON 检查点支持停止/续跑与项目隔离

## 适用场景

- 剧本开拍前自动生成分解表与部门元素清单
- 对未公开剧本在本地离线做安全/特技/亲密戏标记
- 将分解结果导出供 Movie Magic Scheduling 或 Excel 使用

## 场景标签

`多智能体` `文档解析` · 领域:Agent 开发

## 证据(README 行号)

> L46: 1. **Local AI:** All processing happens offline via Ollama, ensuring sensitive IP never leaves the local machine.
> L52: * **Agentic Continuity Audit:** Goes beyond scene-by-scene analysis using a specialized Continuity Agent. This reas

## 星数曲线

```mermaid
xychart-beta
    title "ggvfx/film-breakdown-assistant 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `26bb95e4524c` · [字段定义](../../DATASET.md)*
