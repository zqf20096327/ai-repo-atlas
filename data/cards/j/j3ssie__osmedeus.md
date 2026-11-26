# j3ssie/osmedeus

⭐ 6,671 · Go · MIT · 推送 2026-11-25 · [GitHub](https://github.com/j3ssie/osmedeus) · [官网](https://www.osmedeus.org/) · 个人维护

**面向安全工作者的 YAML 声明式工作流编排引擎**

以 YAML 定义安全自动化工作流的编排引擎，支持 hooks、条件分支与多运行器（host/Docker/SSH），基于 Redis 的 master-worker 分布式执行，内置 80+ 工具函数（nmap 集成、SARIF 解析、CDN/WAF 分类等），提供事件驱动调度、云端扫描（DigitalOcean/AWS/GCP 等）、REST API 与 Web UI。其中包含工具调用型 LLM agent 步骤与 ACP 子进程 agent。安装方式含安装脚本、npm 与 Docker 预编译二进制，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 YAML 工作流，支持 hooks、决策路由与条件分支
- Redis 分布式 master-worker 执行与 webhook/file-watch/cron 触发
- 工具调用型 LLM agent 步骤与 ACP 子进程 agent（Claude Code、Codex 等）
- 80+ 内置函数库与 REST API/Web UI 仪表盘

## 适用场景

- 编排侦察与漏洞扫描等渗透测试工作流
- 以分布式队列批量管理攻击面资产扫描
- 把 LLM agent 步骤嵌入安全自动化流水线
- 在云主机上按需运行扫描并控制成本

## 场景标签

`工作流自动化` `网络安全` · 领域:效率与自动化

## 证据(README 行号)

> L9: Osmedeus is a security focused declarative orchestration engine that simplifies complex workflow automation into aud
> L19: - **Agentic LLM Steps** - Tool-calling agent loops with sub-agent orchestration, memory management, and structured 

## 星数曲线

```mermaid
xychart-beta
    title "j3ssie/osmedeus 星数(近 25 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-25", "2026-11-26"]
    y-axis "stars" 6613 --> 6676
    line [6618, 6619, 6621, 6623, 6625, 6627, 6629, 6634, 6637, 6619, 6644, 6646, 6650, 6651, 6653, 6654, 6656, 6657, 6658, 6660, 6661, 6662, 6664, 6670, 6671]
```

2026-10-24 6,618 → 2026-11-26 6,671（+53）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `92f0a507b766` · [字段定义](../../DATASET.md)*
