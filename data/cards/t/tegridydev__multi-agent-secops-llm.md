# tegridydev/multi-agent-secops-llm

⭐ 10 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/tegridydev/multi-agent-secops-llm) · 个人维护

**将告警/日志目录转化为可溯源安全发现队列的多 Agent 分诊工具**

MASOP 把目录扫描或实时 telemetry 轮询的输入转化为安全发现队列，支持事件 JSONL、Wazuh 导出与 JSON 记录；可对接本地（Ollama/LM Studio/llama.cpp/vLLM）或托管模型，按 triage、身份、端点、漏洞、reviewer 等角色分配 profile。规则层决定入队结果，模型只能从固定清单建议验证步骤，且看不到原始日志、IP、用户名等敏感值；模型失败时离线结果仍可用。不执行文件、不解包、不探测网络。

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

- 离线规则引擎可零依赖运行（无需模型、API key 或 Python 包）
- 支持本地与托管多模型 profile，按角色分配并测试连接
- 模型仅见发现类型/计数/时间跨度，不接触原始日志与敏感值
- 支持静态扫描、目录监听与 JSON telemetry 端点轮询三种运行方式

## 适用场景

- 对 Wazuh 告警导出做本地离线分诊与凭据泄露检查
- 监听目录或轮询 JSON 告警端点做持续发现
- 在断网/保密环境下用本地模型辅助排序待核验事件

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L3: Turn a folder or live feed into a queue of security findings you can trace back to the evidence. Start offline, then
> L26: Start Ollama, LM Studio, llama.cpp or vLLM in its own app or terminal first. In MASOP, choose **Configure agents → 
> L28: Assign profiles to general triage, identity, endpoint, vulnerability or reviewer roles. The rules always decide wha

## 星数曲线

```mermaid
xychart-beta
    title "tegridydev/multi-agent-secops-llm 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `320faf53dc00` · [字段定义](../../DATASET.md)*
