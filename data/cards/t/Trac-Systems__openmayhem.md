# Trac-Systems/openmayhem

⭐ 16 · Rust · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/Trac-Systems/openmayhem) · [官网](https://www.openmayhem.ai) · 组织维护

**去中心化 P2P 推理市场：个人机器卖算力，用户按市场价买推理**

点对点 AI 推理市场：供给方用一条命令（mayhem up --provider）让游戏 PC、Mac、家用服务器或数据中心 GPU 对外提供推理并按 token 计费；用户将任意 OpenAI 兼容客户端指向本地网关 127.0.0.1:11435 购买推理，价格由各信任层级（共四级）的供需按 epoch 浮动，账本公开记录价格与结算。支持聊天、工具调用、视觉、嵌入、图像生成、语音及 ComfyUI 工作流。引擎（llama.cpp/vLLM/TensorRT-LLM/MLX）按硬件自动选择。仅发布源码，本地构建安装，需 Node.js 20+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 供给方一条命令探测硬件、选引擎、拉取模型开始提供服务
- OpenAI 兼容本地网关，价格按 epoch 由市场浮动且可自行复算
- 四级信任层级，Tier 3 机密计算下 prompt 保持私密
- 签名收据与公共账本记录价格、收入与结算
- 同网关支持 ComfyUI 工作流服务

## 适用场景

- 让闲置的游戏 PC 或 Mac 夜间出售推理算力赚取收益
- 用现有 OpenAI 兼容客户端按市场价购买推理，无需中心化云
- Agent 循环通过本地网关调用 8B-14B instruct 模型
- 具备 SEV-SNP+GPU CC 的主机提供 Tier 3 机密计算推理

## 场景标签

`推理引擎` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: OpenMayhem is a peer-to-peer AI inference marketplace. Providers plug in machines and earn on every token they serve
> L24: your OpenAI client ──▶ local gateway (127.0.0.1) ──▶ encrypted P2P session ──▶ a provider's machine
> L125: Point any OpenAI client at `http://127.0.0.1:11435/v1` and go.

## 星数曲线

```mermaid
xychart-beta
    title "Trac-Systems/openmayhem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `8fc02a8cb320` · [字段定义](../../DATASET.md)*
