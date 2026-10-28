# alexei-led/spotinfo

⭐ 165 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/alexei-led/spotinfo) · 个人维护

**跨 AWS/GCP/Azure 的 Spot 实例比价 CLI，内嵌价格快照可离线**

Go 编写的命令行工具，面向需要挑选 Spot/抢占式实例的云成本与 DevOps 人员。按架构、vCPU、内存下限对 AWS、GCP、Azure 三云的真实机型排序，给出价格、节省率与中断风险，并说明每个结论的来源 URL 与文档 SHA-256。价格快照内嵌于二进制，无凭据即可运行，--offline 约 0.1 秒出结果；AWS/Azure 可选读取实时源。限制：GCP/Azure 无可再分发中断数据，风险显示 unavailable；部分功能（placement score、live-risk）需凭据。同时可作为 MCP server 供助手调用。安装提供 Homebrew（macOS），支持 macOS/Linux/Windows 的 AMD64 与 ARM64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三云（AWS/GCP/Azure）统一比价与机型推荐，无凭据可运行
- 价格快照内嵌二进制，--offline 约 0.1 秒应答
- 每个答案标注来源 URL 与文档 SHA-256
- 可作为 MCP server 供 AI 助手直接查询三个工具

## 适用场景

- 按 vCPU/内存/架构下限找三云最便宜的 Spot 机型
- 在无云凭据环境离线查询 Spot 价格
- 让 AI 助手通过 MCP 直接比较 Spot 价格

## 场景标签

 · 领域:云基础设施/成本优化

## 证据(README 行号)

> L25: One command ranks real machines against a real requirement, and says where the number came
> L106: spotinfo is a Model Context Protocol server, so an

## 星数曲线

```mermaid
xychart-beta
    title "alexei-led/spotinfo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 163 --> 166
    line [164, 165, 165]
```

2026-10-18 164 → 2026-10-28 165（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `aa15c30d207a` · [字段定义](../../DATASET.md)*
