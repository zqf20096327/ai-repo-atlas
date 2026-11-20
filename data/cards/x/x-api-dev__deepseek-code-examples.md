# x-api-dev/deepseek-code-examples

⭐ 10 · 推送 2026-09-22 · [GitHub](https://github.com/x-api-dev/deepseek-code-examples) · [官网](https://begin.sh?utm_source=github&utm_medium=ugc&utm_campaign=deepseek-code-examples&utm_content=readme-top&utm_term=tier-r) · 个人维护

**DeepSeek 代码相关可运行示例集：Deep Code 配置与 Ollama 本地调用**

面向想使用 DeepSeek 的开发者的非官方社区示例仓库：一部分生成 Deep Code 终端助手的 settings.json（API 密钥从环境变量读取、文件权限 600，避免密钥进入 dotfiles），另一部分演示通过 Ollama 以 Python、Node.js 和 curl 调用本地 deepseek-coder 模型，覆盖 1.3B/6.7B/33B 三个标签的运行命令。示例基于官方文档中的端点与参数名；仓库自述非 DeepSeek 官方项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从环境变量生成 Deep Code settings.json，密钥不落仓库且文件设为 600
- Python/Node.js/curl 三种方式调用本地 Ollama deepseek-coder
- 提供 1.3B、6.7B、33B 三个模型标签的 ollama run 命令

## 适用场景

- 配置 Deep Code 时把 API 密钥安全地写入设置文件
- 本地用 Python 或 Node 调用 deepseek-coder 模型
- 用 curl 验证本地 Ollama 模型是否已加载

## 场景标签

 · 领域:开发者工具/LLM 示例

## 证据(README 行号)

> L1: # DeepSeek Code examples
> L5: Small, runnable examples for the two things people mean by deepseek code: configuring the Deep Code terminal assista
> L14: |`examples/ollama_chat.py`|Chat with a local `deepseek-coder` model using the `ollama` Python package|

## 星数曲线

```mermaid
xychart-beta
    title "x-api-dev/deepseek-code-examples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `627bfef7bade` · [字段定义](../../DATASET.md)*
