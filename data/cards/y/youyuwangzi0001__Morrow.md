# youyuwangzi0001/Morrow

⭐ 4 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/youyuwangzi0001/Morrow) · 个人维护 · 中文 README

**Windows 本地优先桌面 AI 代理：把一句话需求变成成品文件**

面向 Windows 10/11 x64 的 Electron 桌面 AI 代理：用户描述期望结果，代理读取工作区、写文件、运行命令、自检并产出可打开的文件；会话、记忆、工作区与密钥留在本机，模型由用户自行配置（OpenAI 兼容/Anthropic/订阅通道/Ollama 等）。含 Studio 模块，从一句话前提经可审批的蓝图产出短篇小说、长篇或 30–180 秒漫画短片。提供三级权限、逐回合检查点与文件快照回滚；仅提供未签名的便携版/安装包 Windows 二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种工作模式（chat/work/plan/deep research/long-running goals）与真实文件树、PTY 终端、Git 工作台
- 三级权限与逐次审批危险命令，检查点与写前快照可回滚
- Studio 从蓝图到成稿的流水线：小说、短篇、漫画短片（五轨时间线、节点画布）
- 接入 OpenAI 兼容/Anthropic/订阅通道及本地 Ollama、llama.cpp、LM Studio

## 适用场景

- 让代理把销售导出数据整理成标注异常的 HTML 报告
- 在本地工作区内让 AI 完成写作、研究等长任务
- 从一句话前提推进小说或漫画短片的创作与成片

## 场景标签

`AI 助手` `AI 写作` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L4:  A local-first AI workspace for Windows that turns a request into a finished file.
> L16: Morrow is a desktop AI agent for Windows 10/11 x64. You describe the result you want; it reads the workspace, write
> L43: - API keys for OpenAI-compatible and Anthropic providers, subscription channels, and local models through Ollama, l

## 星数曲线

```mermaid
xychart-beta
    title "youyuwangzi0001/Morrow 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-12", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0fe24b138402` · [字段定义](../../DATASET.md)*
