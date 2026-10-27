# shootthesound/comfyui-mesh

⭐ 126 · Python · 推送 2026-05-17 · [GitHub](https://github.com/shootthesound/comfyui-mesh) · 个人维护

**ComfyUI 双 GPU 分布式推理组件：拆分 FLUX.2/LTX 2.3 跨机运行**

由 Icarus（ComfyUI 客户端节点）与 Daedalus（后端服务器）组成，将 FLUX.2 Dev/Klein 9B 与 LTX 2.3 的 transformer 块拆分到两块 NVIDIA GPU 上（跨局域网/VPN 或同机双卡），中间的激活数据用 NVENC 硬件编码为 HEVC 压缩后经网络传输，接收端用 NVDEC 还原。支持 ComfyUI 各类 LoRA 格式与转发。限制：仅支持所列模型，其他架构（Wan、FLUX.1、SD3.5 等）在路线图上；需具备 NVENC 的 NVIDIA 显卡。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FLUX.2 Dev/Klein 9B 与 LTX 2.3 的前后半拆分跨 GPU 运行
- 用 NVENC HEVC 将激活张量压缩 3–10 倍后经网络传输（NVDEC 解码）
- LAN/VPN/同机双卡三种拓扑，无需 NVLink
- 支持 ComfyUI 的多种 LoRA 格式及两侧分别加载

## 适用场景

- 显存不够单卡跑大模型时，用两块显卡或两台机器分担
- 局域网/VPN 上把家中多台机器的 GPU 拼起来跑 FLUX.2 或 LTX 视频生成
- 在 ComfyUI 工作流中以节点方式卸载模型后端块

## 场景标签

`图像生成` `视频生成` `推理引擎` · 领域:内容生成

## 证据(README 行号)

> L3: **ComfyUI Mesh : Icarus** *(the ComfyUI client node)* ↔
> L6: **Split a diffusion model across two GPUs — either over a gigabit
> L42:                 │     Icarus      │   NVENC HEVC wire   │    Daedalus     │

## 星数曲线

```mermaid
xychart-beta
    title "shootthesound/comfyui-mesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-27 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6a11c7003b28` · [字段定义](../../DATASET.md)*
