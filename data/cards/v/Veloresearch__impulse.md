# Veloresearch/impulse

⭐ 34 · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/Veloresearch/impulse) · [官网](https://veloresearch.com/impulse) · 组织维护

**本地运行 GGUF 模型的桌面应用：长记忆、电脑操作与 OpenAI 兼容 API**

Velocity 公司开发的 Windows/Linux 桌面应用，加载任意 GGUF 模型并按显卡自动选择运行方式。提供带引用的联网聊天、语音转录、文件问答、Python 沙箱、图表绘制与计算机操作（读取窗口控件、四级权限控制）。核心机制 Momentum 可让 8K 窗口的模型覆盖最多 3200 万 token 的本地材料，不使用嵌入与向量数据库；上下文以可移植 .mfyc 文件保存。同时对外提供 OpenAI 兼容 API 与 MCP 服务器供其他应用调用。无账户、无遥测；计算机操作功能仅限 Windows 且为新功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Momentum 记忆：8K 窗口模型覆盖最多 32M token 本地文档，不用嵌入与向量库
- 对外提供 OpenAI 兼容 API 地址与 MCP，供其他应用调用
- 计算机操作：直读窗口控件而非像素猜测，四级权限、可随时停止
- 联网搜索先行作答，每条声明带编号引用溯源

## 适用场景

- 在本机离线运行 GGUF 模型进行带来源的联网问答
- 把整个文件夹或代码仓库加入记忆后跨全部内容提问
- 让本地模型代为操作电脑上的应用（Windows，需授权）
- 通过 OpenAI 兼容 API 让其他 agent 应用接入本地模型

## 场景标签

`GUI 自动化` `推理引擎` `语音识别` `文档问答` · 领域:效率与自动化

## 证据(README 行号)

> L52: - **One app for running models locally.** Download or add a GGUF model, and Impulse chooses how it runs on your gra
> L173:  Connect: the API address copied, the key, and ready-made curl, Python and JavaScript requests Connect : one addre
> L174:  Apps with opencode and Hermes Agent, then Plugins and the Files preset opening Apps and Plugins : agents in one c

## 星数曲线

```mermaid
xychart-beta
    title "Veloresearch/impulse 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-29 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2c1ced5e31b6` · [字段定义](../../DATASET.md)*
