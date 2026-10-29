# Michael-A-Kuykendall/rustchain

⭐ 25 · Rust · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/Michael-A-Kuykendall/rustchain) · [官网](https://rustchain.dev) · 个人维护

**Rust 工作流转译执行框架：迁移并运行 LangChain/Airflow 等工作流**

用 Rust 实现的工作流迁移与执行框架：通过转译器将已有的 LangChain 脚本、Airflow DAG、GitHub Actions、Kubernetes 与 Docker Compose 定义转换为统一的 mission.yaml 格式，再由 rustchain run 原生执行。转换保留步骤、依赖关系、配置与密钥引用，并支持格式自动检测；也可直接用 YAML 编写 mission。要求 Rust 1.70+ 从源码编译，AI 功能可选接 Ollama 等兼容 LLM 后端。项目采用 MIT/Apache-2.0 双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 5 种来源格式转译为统一 mission.yaml（LangChain/Airflow/GitHub Actions/Kubernetes/Docker Compose）
- 转译保留步骤、depends_on 依赖、参数与环境变量引用
- 格式自动检测（rustchain transpile auto）
- 提供 CLI：运行、转译、mission 校验与管理

## 适用场景

- 把已有 LangChain/Airflow 工作流迁移到 Rust 原生运行时
- 统一管理跨平台定义的 CI/编排/部署工作流
- 不重写现有文件直接生成可执行 mission

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L26: |**LangChain** (Python)|✅ Supported|`rustchain transpile lang-chain script.py`|
> L84: |LangChain|`from langchain`, `from openai`|Chains, agents, tools, prompts|
> L151: - **Optional**: Ollama or compatible LLM backend for AI features

## 星数曲线

```mermaid
xychart-beta
    title "Michael-A-Kuykendall/rustchain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `1e2764c6e08f` · [字段定义](../../DATASET.md)*
