# branover/hexgraph

⭐ 21 · Python · AGPL-3.0 · 推送 2026-08-15 · [GitHub](https://github.com/branover/hexgraph) · 个人维护

**自托管 AI 漏洞研究工作台：对二进制/固件做分析并记录到类型化图谱**

本地自托管的安全研究工作台：输入二进制或固件镜像后，由 AI agent 在无网络的 Docker 沙箱中执行反编译、字符串/导入分析、模糊测试与 PoC 验证等工具，将结果以带类型边的图谱（目标/函数/套接字/假设/发现）存入 SQLite，并附研究日志与假设工作清单。模型接入 BYOK：Anthropic API key、本地 Claude Code 或离线 mock 后端。模型只调度工具，不接触原始目标字节。提供 Web UI（仅监听 localhost）与 MCP 接口，pre-1.0 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 目标→任务→结构化发现→图谱→派生下一任务的闭环
- 所有目标解析与分析在无网络、限资源的沙箱容器中执行，默认仅静态
- 类型化图谱 + 时间戳研究日志 + 假设工作清单共享工作记忆
- BYOK：Anthropic key / 本地 Claude Code / 免 key 离线 mock 三种后端

## 适用场景

- 对固件与二进制目标做 AI 辅助的漏洞研究并沉淀结构化发现
- 通过 Claude Code/Codex 等 agent 经 MCP 驱动沙箱化逆向分析
- 运行覆盖率引导的模糊测试活动并对崩溃做去重与复验

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: driven by whatever model access you already have, and writes every result down as a structured
> L140: an agent loop. The model asks for sandboxed tools (decompile, strings, imports, xrefs, fuzz), HexGraph
> L156: |`anthropic`|`--backend anthropic` / `HEXGRAPH_LLM_BACKEND=anthropic`|Your own key via `ANTHROPIC_API_KEY` (env or

## 星数曲线

```mermaid
xychart-beta
    title "branover/hexgraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-20"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-20 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `03b04365b712` · [字段定义](../../DATASET.md)*
