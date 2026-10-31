# esephaneli/portable-ai

⭐ 14 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/esephaneli/portable-ai) · 个人维护 · 中文 README

**USB 便携全离线 AI 助手：加密历史、本地 RAG**

从 USB 直接运行的离线 AI 聊天助手：基于 llama-cpp-python 运行 Trendyol-LLM 7B（Qwen2.5 上 13B 土耳其语 token 继续预训练），支持 PDF/DOCX/TXT 上传的 RAG 对话，提供 9 种预设角色模式。聊天历史与文档经 SQLCipher AES-256 加密，绑定 USB 卷序列号，数据库被复制到其他 USB 无法打开；passphrase 仅存内存。面向 KVKK 合规需求的土耳其律师、医生、会计等专业人士及封闭环境机构。通过 PyInstaller 打包为免安装包，模型约 4.7 GB；已知限制：无 OCR、DOCX 仅提取文本与表格。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AES-256 加密聊天历史并绑定 USB 卷序列号（他处无法解密）
- 本地 llama-cpp-python 推理 Trendyol-LLM 7B，首次 embedding 下载后 100% 离线
- PDF/DOCX/TXT 文档 RAG，numpy 暴力向量检索
- PyInstaller --onedir 打包，无需 Python 环境即可运行

## 适用场景

- 律师/医生/会计等在无外发数据前提下与 LLM 对话
- 在离线封闭环境（如公共机构）中使用 AI 助手
- 随身携带加密的对话历史与文档知识库

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L22: - 🔒 **AES-256 sifreli sohbet gecmisi** — sqlcipher + passphrase + USB volume serial
> L25: - 🧠 **Trendyol-LLM 7B** — Qwen2.5 7B uzerine 13B Turkce token continued pretraining
> L26: - 💾 **%100 offline** — internet gerekmez (ilk embedding download haric, sonrasinda kapali)

## 星数曲线

```mermaid
xychart-beta
    title "esephaneli/portable-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a70c57146e1d` · [字段定义](../../DATASET.md)*
