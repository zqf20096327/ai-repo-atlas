# pranavkumaarofficial/nlcli-wizard

⭐ 33 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/pranavkumaarofficial/nlcli-wizard) · [官网](https://www.reddit.com/r/LocalLLaMA/comments/1or1e7p/i_finetuned_gemma_3_1b_for_cli_command/) · 个人维护

**给 Python CLI 工具加自然语言 `-w` 标志的本地 SLM 流水线**

为库维护者提供一套四步流水线，让 CLI 工具支持以英文描述生成命令：从 flag 语法生成训练集、做四通道污染审计、QLoRA 微调 1B 基座模型、量化为 4-bit GGUF 后由 llama.cpp 在 CPU 上推理，全程离线无需 API key。当前以 Docker 为唯一已实现示例（5,000 例训练集、116 条人工 held-out，微调适配器准确率 62.9%）。限制：权重尚不可下载（HF 仓库私有）、per-library 打包未实现、三个以上 flag 组合基本未解决。以源码 + venv 方式安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四步流水线：数据生成→污染审计→QLoRA 微调→GGUF 量化
- CPU 本地推理，无需 GPU/网络/API key（1.85s 出答）
- 无第三方依赖的评测代码，附带逐条生成记录可复查
- GGUF 头检查脚本可检验小模型量化格式

## 适用场景

- 库维护者为自家 CLI 工具训练并附带一个命令翻译模型
- 在离线/air-gapped 环境用英文描述直接生成 docker 命令
- 研究者复现小模型微调评测结果（可无 GPU 回放）

## 场景标签

`微调` `模型量化` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L9: **A pipeline for giving any Python CLI tool a `-w` flag that takes plain English.**
> L34: The product here is not the Docker model. It is the four steps that produce one, so a
> L46: **3. Fine-tune.** QLoRA on a 1B base model, one adapter per tool, on a free Colab T4 or

## 星数曲线

```mermaid
xychart-beta
    title "pranavkumaarofficial/nlcli-wizard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `df84b250452a` · [字段定义](../../DATASET.md)*
