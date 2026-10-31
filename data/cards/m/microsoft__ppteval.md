# microsoft/ppteval

⭐ 16 · Python · MIT · 推送 2026-09-19 · [GitHub](https://github.com/microsoft/ppteval) · [官网](https://microsoft.github.io/ppteval/) · 组织维护

**评测计算机使用 Agent 的 PowerPoint 任务基准**

微软发布的 PPT-Eval 基准，用于在 PowerPoint 任务上评测 GUI 式 computer-use agent 与 CLI 式 agent。支持 Docker 沙箱运行 GUI agent（通过 OneDrive/PowerPoint Online 准备并规范化 .pptx 数据），也支持 Claude Code CLI 预设在本地工作区内直接编辑 .pptx 文件。评分使用可配置的 VLM 验证器（默认 Claude 模型），以 pip/uv 安装 Python 包形式提供，需设置 API key 等环境变量，附论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 GUI 式 computer-use agent 与 CLI 式 agent 两类评测
- hydrate_data.py 经 OneDrive/PowerPoint Online 规范化 .pptx 元数据以减少验证误差
- 多预设配置（cua/claude-4-sonnet/claude-code-opus 等），支持并发评测
- Docker 沙箱用于 GUI agent，CLI agent 无需 Docker

## 适用场景

- 评测 agent 在 PowerPoint 编辑任务上的表现
- 对比不同模型/agent 框架的办公软件操作能力
- 复现论文基准结果或扩展新 agent 配置

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A benchmark to evaluate Computer-Use Agents on PowerPoint tasks.
> L31: RUBRIC_DEFAULT_LLM="anthropic/claude-sonnet-4-20250514" # Model used for VLM calls in verifiers

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/ppteval 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8441db63c96e` · [字段定义](../../DATASET.md)*
