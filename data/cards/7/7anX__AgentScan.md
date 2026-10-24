# 7anX/AgentScan

⭐ 109 · Go · MIT · 推送 2026-08-01 · [GitHub](https://github.com/7anX/AgentScan) · 个人维护 · 中文 README

**一条命令盘点 MCP、A2A Agent Card 与 LLM 开放接口暴露面**

用 Go 编写的安全扫描工具：在端口发现基础上进一步识别服务是否为 MCP Server、A2A Agent 或开放的 LLM 推理接口，输出工具列表、Agent 能力、模型列表与认证状态，覆盖 Ollama、vLLM、llama.cpp 等 25 种推理框架的识别，并检测蜜罐信号。提供全协议、单协议扫描子命令与并发/超时参数，可与 masscan 组合使用。支持源码编译与预编译二进制两种安装方式，面向合法授权的企业安全建设工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 识别 MCP / A2A / LLM 三类 AI 协议服务及认证状态
- 支持 25 种推理框架的开放接口识别
- 提供 MCP 蜜罐信号检测与 OAuth 2.0 发现
- 可与 masscan 端口发现结果组合流水线使用

## 适用场景

- 企业安全团队盘点内网暴露的 MCP/A2A/LLM 服务
- 对已授权目标做 AI 协议层面的暴露面巡检
- 端口扫描后进一步确认服务是否为 AI 推理接口

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: 传统端口扫描器只告诉你"这里有个 HTTP 服务"。AgentScan 继续往下走一层：判断这个服务是不是 MCP、是不是 A2A Agent、是不是开放的 LLM 接口，并输出可用工具、Agent 能力、模型列表和认证状态。
> L17: |MCP Server|Streamable HTTP、HTTP+SSE legacy、工具/资源/提示词列表、认证状态、需认证 MCP Server 的 OAuth 2.0 发现、蜜罐信号|
> L18: |A2A Agent|Agent Card、skills、interfaces、无认证 JSON-RPC 可达性|
> L19: |LLM 开放接口|Ollama、vLLM、SGLang、TGI、llama.cpp、Xinference、LiteLLM、FastChat、LocalAI、LM Studio、LMDeploy 等 25 种推理框架|

## 星数曲线

```mermaid
xychart-beta
    title "7anX/AgentScan 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 107 --> 110
    line [108, 109, 109]
```

2026-10-18 108 → 2026-10-24 109（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `63aec687149d` · [字段定义](../../DATASET.md)*
