# Intelligent-CAT-Lab/AlphaTrans

⭐ 38 · Java · NCSA · 推送 2025-12-20 · [GitHub](https://github.com/Intelligent-CAT-Lab/AlphaTrans) · [官网](https://doi.org/10.5281/zenodo.13826582) · 组织维护

**仓库级 Java→Python 代码翻译与验证的论文 artifact（FSE 2025）**

FSE 2025 论文 AlphaTrans 的 artifact 仓库：神经符号组合式方法将 Java 项目片段按逆调用图顺序翻译为 Python，并经语法检查、GraalVM 与测试执行验证；流程含 CodeQL 静态分析建库、程序分解生成 schema、类型翻译、骨架构建与重组。支持 OpenAI 模型（gpt-4o）与 deepseek-coder 等开源模型（ollama/vLLM 等端点服务），通过 model_configs.yaml 配置。以 Dockerfile 交付全部依赖，提供脚本复现论文五个 RQ 结果及翻译新项目，预计算结果存于 Zenodo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | NCSA |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按逆调用图顺序的片段化翻译与逐级验证（语法/GraalVM/测试执行）
- CodeQL 数据库创建与静态分析驱动的 schema 构建
- 支持 OpenAI 模型与 ollama/vLLM 服务的开源模型，经 model_configs.yaml 配置
- 提供 Dockerfile 复现环境与五个研究问题（RQ1-RQ5）的复现脚本

## 适用场景

- 复现 FSE 2025 论文中 AlphaTrans 的实验结果
- 将新的 Java 项目翻译为 Python 并做测试验证
- 分析测试分解与程序变换对翻译效果的影响

## 场景标签

 · 领域:软件工程/代码翻译

## 证据(README 行号)

> L6: Artifact repository for the paper _AlphaTrans: A Neuro-Symbolic Compositional Approach for Repository-Level Code Tra
> L25: AlphaTrans currently supports prompting OpenAI models (e.g., `gpt-4o-2024-11-20`) and open-source models (e.g., `de
> L40: These scripts will translate the project fragment by fragment in reverse-call graph order and store translations in

## 星数曲线

```mermaid
xychart-beta
    title "Intelligent-CAT-Lab/AlphaTrans 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2fa543779048` · [字段定义](../../DATASET.md)*
