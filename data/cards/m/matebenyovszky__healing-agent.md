# matebenyovszky/healing-agent

⭐ 26 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/matebenyovszky/healing-agent) · 个人维护

**Python 库：函数抛异常时用 AI 自动改写修复并重跑**

通过装饰器使用的代码自愈库：被装饰的 Python 函数抛异常或主动请求修复时，捕获源码、参数、局部变量与 traceback 等上下文，交由 LLM（Azure OpenAI/OpenAI/Anthropic/Ollama/LiteLLM）生成修复代码，备份原件后应用并重跑；失败则回滚并重新抛出原异常。另支持数据漂移场景下适配加载器使新旧格式并存、GitHub issue 升级与草稿 PR 交付、密钥脱敏。README 声明不建议用于生产环境；AUTO_FIX 默认开启，AUTO_SYSCHANGE 默认关闭。嵌套函数不可修复，支持 Python 3.10–3.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 装饰器方式自动捕获异常上下文、生成修复并重跑（含 async 与类方法）
- Data Healing：适配结构漂移的输入，新旧格式同时可用，缺失必需数据时拒绝编造
- 多提供商支持（Azure OpenAI、OpenAI、Anthropic、Ollama、LiteLLM），发送前脱敏密钥
- 修复成功可生成草稿 PR，失败可去重地开 GitHub issue

## 适用场景

- 夜间定时任务抛异常时自动修复重跑，无需人工值守
- CSV/API 等输入格式漂移后自动适配加载逻辑
- 在 Python 3.10–3.13 项目中零配置引入（import、装饰、运行）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: Healing Agent is a deliberately small code-healing library: decorate a Python function, and when it raises, an AI a
> L20: - 💡 AI-generated fixing hints and repaired code, multi-provider (Azure OpenAI, OpenAI, Anthropic, Ollama, LiteLLM)

## 星数曲线

```mermaid
xychart-beta
    title "matebenyovszky/healing-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `281f91ee18f7` · [字段定义](../../DATASET.md)*
