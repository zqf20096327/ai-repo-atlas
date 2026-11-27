# byjameson/stream-finetune

⭐ — · [GitHub]() · 个人维护

**让 6 GB 笔记本 GPU 微调 32B 模型的流式 NF4 训练器**

一个面向显存不足场景的训练引擎：NF4 权重从磁盘 mmap，每次仅加载一个 transformer 块到 GPU，反向传播通过重计算完成，基座冻结、只训练 LoRA 适配器。提供 `streamft` CLI（pip 安装）、fit 规划器根据测得的 VRAM/RAM 选择驻留块窗口、fp16 老卡路径、导出 GGUF 在浏览器端 wasm 推理，以及 OpenAI 兼容的 `/v1/chat/completions` 本地服务。附大量实测数据与训练配方文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式 NF4 训练：权重 mmap 自磁盘，逐块驻留 GPU，基座冻结仅训 LoRA
- 免费 fit 规划器：输入模型 id 与 VRAM 大小，输出能否装下及实测速度
- 适配器 4-bit 打包后共享基座部署，LAN 服务提供 OpenAI 兼容端点
- 老 GPU（Pascal/Turing 无 bf16）提供 fp16 训练路径

## 适用场景

- 在 6 GB 显存的笔记本上微调 7B–32B 模型
- 多行为适配器共享一个量化基座分发部署
- 评估某个模型能否装进自己的显存预算
- 把合并后的小模型导出 GGUF 在浏览器中运行

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: A small training engine that fine-tunes models that **do not fit in VRAM**. The NF4
> L197: - `streamft/stream_quant_lora.py` — the streaming trainer: base frozen, LoRA trainable,
> L239: streamft merge --model Qwen/Qwen2.5-0.5B --adapter checkpoints/cpu_cookbook --out merged/q05

## 星数曲线

```mermaid
xychart-beta
    title "byjameson/stream-finetune 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-21", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `196c261cde60` · [字段定义](../../DATASET.md)*
