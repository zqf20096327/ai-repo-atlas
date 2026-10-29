# TenchiNeko/standalone-orchestrator

⭐ 22 · Python · MIT · 推送 2026-09-23 · [GitHub](https://github.com/TenchiNeko/standalone-orchestrator) · 个人维护

**本地 LLM 上的自主多智能体编码系统：计划→构建→测试→修复**

无框架依赖的 Python 编排器，把任务描述转为有界的 plan→build→test→RCA 循环，在本地 Ollama 端点（默认 Qwen 80B 做规划/代码生成、7B/14B 做探索/测试）上运行。每文件多候选温度采样、语法约束的结构化编辑修复、AST 依赖图级联重建；附四层知识栈（RAG 知识库、librarian、ACE 式 playbook 守护进程、self-play 训练数据）。README 自述为实验性系统，最低需 24GB VRAM 单 GPU，通过 git clone 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 有界编排循环：迭代上限与 DoD 验证门，未解决任务以 handoff 收尾而非无限重试
- 多候选采样 + 语法约束 JSON 编辑修复，自动回退 SEARCH/REPLACE
- AST 依赖图级联重建与 AST 签名提取（约 200 token 代替完整源码）
- 四层知识栈：RAG 知识库、7B librarian、ACE 式 subconscious 守护进程、self-play JSONL 数据

## 适用场景

- 在自有 GPU 上自主完成小型编码任务（CLI、REST API 等）
- 以可读 Python 代码路径替代黑盒 agent 框架做编排实验
- 收集 (需求→代码) JSONL 对用于后续 QLoRA 微调

## 场景标签

`编码 Agent` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9:  A framework-free Python orchestrator for bounded, multi-agent coding workflows across local language models.
> L17: Standalone Orchestrator turns a task description into an explicit plan → build → test → root-cause-analysis loop. E
> L44: 5/5 tasks passing — 217/249 tests (87%). All DoD criteria met across every level. The system handles everything fro

## 星数曲线

```mermaid
xychart-beta
    title "TenchiNeko/standalone-orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d925b7aade0f` · [字段定义](../../DATASET.md)*
