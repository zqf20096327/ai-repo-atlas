# mareforma/mareforma

⭐ 15 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/mareforma/mareforma) · [官网](https://www.mareforma.com/) · 组织维护

**记录并核验 AI 科学发现的数据依据的本地优先库**

面向 AI scientist/多 agent 科研工作流的本地优先 Python 库：将发现记录为带签名的 claim，claim 之间引用或反驳形成知识图谱。核心机制是在 I/O 边界（requests/httpx/pandas/io.open 等）观察进程实际读取的文件与网络调用，计算 finding 的 GROUNDED/UNGROUNDED/OPAQUE 判定，替代模型自报的可信度。提供 CLI：diagnose 观察单次运行、verify 按 CI 退出码复核签名与依据、map 展示信任属性（有效独立性等）、mcp serve 以只读 MCP 服务暴露项目。数据存本地 SQLite，公共日志为可选项。

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

- 在 requests/httpx/io.open/pandas/polars 等 I/O 边界观察运行，计算 GROUNDED/UNGROUNDED 判定
- 签名 claim 知识图谱：每次读取时复核签名，篡改在查询时被捕获
- trust map 报告有效独立性（模型/数据/签名者差异）与 UNVERIFIABLE 情形
- verify 提供稳定退出码（0 通过/1 篡改/2 不可验证）用于 CI 门禁

## 适用场景

- 拦截 AI agent 未读数据、凭记忆作答并编造引用的静默失败
- 科研团队以签名 claim 记录发现并公开可验证的溯源
- 在 CI 中以 mareforma verify 门禁校验 finding 的数据依据

## 场景标签

`知识图谱` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L18: Mareforma is a local-first library where AI scientists record their findings as claims. Each claim cites the claims
> L100: |**Grounding check**|Computes whether a finding's step actually accessed the data it cites, or leaned on the model
> L103: |**Diagnose a run**|`mareforma diagnose -- python run.py` runs a target under the observer and reports what data a

## 星数曲线

```mermaid
xychart-beta
    title "mareforma/mareforma 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `db0fc0d0c8bc` · [字段定义](../../DATASET.md)*
