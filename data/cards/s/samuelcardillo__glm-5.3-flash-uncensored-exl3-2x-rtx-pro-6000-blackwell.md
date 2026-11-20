# samuelcardillo/glm-5.3-flash-uncensored-exl3-2x-rtx-pro-6000-blackwell

⭐ 10 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/samuelcardillo/glm-5.3-flash-uncensored-exl3-2x-rtx-pro-6000-blackwell) · 个人维护

**在双 RTX PRO 6000 Blackwell 上复现部署 GLM-5.3 Flash Uncensored 的配方**

一个修订版锁定的部署配方仓库：以 EXL3 量化加 DFlash2 投机解码在两张 NVIDIA RTX PRO 6000 Blackwell 96 GB GPU 上运行 GLM-5.3 Flash Uncensored（去审查版本）检查点，提供 git clone 后经 Docker 启动的脚本链（preflight/serve/verify/stop），并给出 systemd 用户服务安装器。对外暴露 OpenAI 兼容 API，默认仅绑定 loopback 且无内置认证。仅限指定的两卡配置，其他 GPU 与驱动分支被声明为不合格；公开配方未经新的 GPU 启动验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TP2/EXL3 4 bpw 量化加 DFlash2 K3 投机解码的完整启动配置
- preflight 脚本对每个锁定文件做哈希校验（约 178 GB 全量读取）
- 提供 systemd 用户服务安装器与启动/停止/验证脚本
- OpenAI 兼容文本、推理与原生工具调用接口

## 适用场景

- 在两台 RTX PRO 6000 Blackwell 工作站上本地部署该去审查模型
- 通过 OpenAI 兼容 API 在局域网或 Tailscale 内调用本地模型
- 需要可复现的锁定版本模型部署与哈希校验流程

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Revision-pinned **v0.8** recipe based on a live implementation tested on two NVIDIA RTX PRO 6000 Blackwell 96 GB GPU
> L64: ./scripts/serve.sh
> L94: curl http://127.0.0.1:8000/v1/chat/completions \


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `096b1fdc9865` · [字段定义](../../DATASET.md)*
