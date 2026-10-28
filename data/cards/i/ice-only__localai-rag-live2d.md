# ice-only/localai-rag-live2d

⭐ 21 · Python · MIT · 推送 2026-07-30 · [GitHub](https://github.com/ice-only/localai-rag-live2d) · 个人维护 · 中文 README

**带 Live2D 二次元形象的本地 RAG 桌面 AI 聊天伴侣**

基于 PyQt5 的桌面 AI 伴侣应用：通过 llama-cpp-python 加载 Qwen 量化 GGUF 模型（Vulkan GPU 加速，CPU 可运行），结合 bge-small-zh-v1.5 嵌入与 ChromaDB 向量库实现本地 RAG 检索，docs/ 目录文件增删自动同步索引。角色以 Live2D 透明无边框窗口常驻桌面，可拖动交互；对话记忆按用户隔离以 JSON 持久化并按 Token 预算裁剪；另支持 QQ OneBot v11 接入。面向个人用户，数据全程本地，需 Python 3.10+、8GB 以上内存与约 5GB 磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- llama-cpp-python 加载 Qwen 量化 GGUF，Vulkan GPU 加速，CPU 亦可运行
- RAG 本地检索：bge-small-zh-v1.5 + ChromaDB + watchdog 文件自动同步
- Live2D 角色透明置顶窗口，可拖动，系统托盘控制
- 对话记忆 JSON 持久化，多用户隔离，Token 预算自动裁剪

## 适用场景

- 本地运行二次元形象 AI 聊天伴侣，数据不上传云端
- 把 txt/md/pdf 文档放进 docs/ 目录即可让 AI 引用个人知识
- 通过 QQ OneBot v11 在 QQ 端与同一 AI 对话

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: 基于量化千问 4B 模型 + 本地 RAG 文档检索 + Live2D 二次元形象的桌面 AI 伴侣。
> L10: - **本地 LLM 推理**：Qwen3.5-4B GGUF 量化模型，Vulkan GPU 加速，CPU 亦可流畅运行
> L72: - **Model 层**：llama-cpp-python 加载 GGUF，Vulkan 后端加速，ChatML 格式对话

## 星数曲线

```mermaid
xychart-beta
    title "ice-only/localai-rag-live2d 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e5ab5bf85c4c` · [字段定义](../../DATASET.md)*
