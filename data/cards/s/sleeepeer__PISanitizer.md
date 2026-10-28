# sleeepeer/PISanitizer

⭐ 20 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/sleeepeer/PISanitizer) · [官网](https://arxiv.org/abs/2511.10720) · 组织维护

**通过提示净化防御长上下文 LLM 提示注入攻击的研究代码**

EMNLP 2026 论文 PISanitizer 的官方仓库：一种针对提示注入攻击的预防性防御方法，通过对长上下文输入进行提示净化（prompt sanitization）来防护 LLM。默认代码使用 meta-llama/Llama-3.1-8B-Instruct，需 HuggingFace 登录。提供 Python 库式调用接口，并附带 prepare_data.py 与 run.py 脚本用于复现实验；可选配置 Azure OpenAI 作为 LLM 评估裁判，实验会并行运行大量进程。

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

- 针对长上下文 LLM 的提示注入防御（提示净化）
- 以 Python 包形式导入使用（from PISanitizer import pisanitizer）
- 提供数据准备与实验复现脚本，支持并行运行
- 可选接入 Azure OpenAI 作为 LLM-as-a-judge 评估

## 适用场景

- 在长上下文 LLM 应用中净化输入以防提示注入
- 复现论文的提示注入防御实验
- 研究提示注入防御方法的效果

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7:  A prevention defense to prompt injection attacks.
> L34: injected_context = """PISanitizer: Preventing Prompt Injection to Long-Context LLMs via Prompt Sanitization

## 星数曲线

```mermaid
xychart-beta
    title "sleeepeer/PISanitizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `71718b6da6fc` · [字段定义](../../DATASET.md)*
