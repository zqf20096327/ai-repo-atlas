# dumbpabloo/BlackEclipse-V1.0

⭐ 7 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/dumbpabloo/BlackEclipse-V1.0) · [官网](https://dumbpabloo.github.io/BlackEclipse-V1.0/) · 个人维护

**面向投资者的本地优先金融 agentic 自动化运行框架**

桌面端 agentic harness：模型负责规划与解释，确定性 Python 引擎负责指标、估值、风险与回测计算，每个结论附带来源凭据，无法溯源时返回 UNAVAILABLE。功能覆盖公司研究、市场筛选、策略回测（anti-lookahead、walk-forward、Deflated Sharpe）、组合管理、定时 bot 与工作流，交易需经单次审批、保证金上限与 kill switch 的受控通道。模型可插拔（OpenAI/Anthropic/Ollama 等），无需管理员权限，账号与遥测均无。Windows 安装包为主，macOS/Linux 构建未发布；PyPI 包尚未上线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型不产出数字：所有计算由带公式、输入与种子的确定性 Python 引擎完成
- 策略回测支持 anti-lookahead、walk-forward 与 Deflated Sharpe 过拟合检查
- 工具声明权限与效果类别，交易执行需单次审批并配备 kill switch
- 模型可插拔：OpenAI/Anthropic/Google/Mistral/Groq/OpenAI 兼容端点或本地 Ollama

## 适用场景

- 估值公司与同业比较并获得带引用的报告
- 编写策略并运行回测得到权益曲线与评级
- 定时运行早间市场简报 bot
- 导入券商交易对账并分析组合风险敞口

## 场景标签

`金融量化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L20: Black Eclipse puts the pieces behind one agentic harness: a model that plans and
> L40: cannot declare them is not published. Models are interchangeable — OpenAI, Anthropic,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `dd980e51b692` · [字段定义](../../DATASET.md)*
