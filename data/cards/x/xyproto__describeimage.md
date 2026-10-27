# xyproto/describeimage

⭐ 22 · Go · BSD-3-Clause · 推送 2026-06-05 · [GitHub](https://github.com/xyproto/describeimage) · 个人维护

**用本地 Ollama 视觉模型描述图片内容的命令行工具**

Go 编写的命令行工具，调用本地或 OLLAMA_HOST 指定服务器上的 Ollama 服务，对给定图片生成文字描述。默认视觉模型为 qwen2.5vl:3b（约 3.5GB），可通过 llm-manager 配置文件、/etc/llm.conf 或 -m 参数切换模型（如 gemma3:4b、llava-llama3:8b）。运行需 Ollama 服务在线且内存/CPU/GPU充足，构建需 Go 1.22+，通过 go install 安装。BSD-3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 Ollama 视觉模型为图片生成文字描述
- 默认模型 qwen2.5vl:3b，支持多模型切换（-m 标志或 llm-manager 配置）
- 支持本地或 OLLAMA_HOST 远程服务器上的 Ollama 服务

## 适用场景

- 为图片生成替代文本以辅助无障碍访问
- 在命令行批量获取图片的文字描述
- 利用本地模型离线描述图片内容

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: Use LLMs that are running locally (or on a server defined in `OLLAMA_HOST`) to describe the given images.
> L11: * Ollama (the service must be up and running, and there must be enough memory and CPU and/or GPU available to be ab

## 星数曲线

```mermaid
xychart-beta
    title "xyproto/describeimage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7bfefbd33f89` · [字段定义](../../DATASET.md)*
