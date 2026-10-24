# MigoXLab/webqa-agent

⭐ 236 · Python · Apache-2.0 · 推送 2026-07-02 · [GitHub](https://github.com/MigoXLab/webqa-agent) · 组织维护 · 中文 README

**面向工程师的自主 Web 测试 Agent：一句话目标即驱动浏览器完成测试**

AI 驱动的自动化 Web 测试代理：通过多模态页面理解直接识别页面元素，无需编写测试脚本与维护选择器。提供三种测试形态——Flash 模式（一句自然语言目标秒级执行）、Standard Generate（AI 发现→动态生成→执行）、Run 模式（执行 YAML 用例做回归）。支持 CLI、Docker/K8s 全栈 Web 平台部署，内置 MCP Server 与 Skill，可接入 Cursor、Claude Code 等 IDE，由 AI 编码助手发起测试。平台内置 API Key 管理与 HTML 报告。Web 仪表盘目前仅提供中文界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种测试形态：Flash 秒级探索 / Standard Generate 动态生成 / Run YAML 回归执行
- 多模态元素识别，零 CSS/XPath 选择器维护
- 内置 MCP Server（webqa-mcp-server）与 Skill 包，接入 Cursor / Claude Code / OpenClaw
- CLI、Docker Compose、Kubernetes 三类部署方式，内置技能含 nuclei-scan 安全扫描

## 适用场景

- 不写脚本，用一句自然语言描述目标即完成网页冒烟测试
- 新功能探索式 QA 与无 PRD 场景下的测试发现
- 通过 Cursor / Claude Code 让 AI 编码助手直接运行浏览器测试
- 回归测试：以 YAML 用例做可重复执行与断言校验

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L29:  🤖 WebQA Agent is a fully automated web testing agent with multimodal page understanding — no test scripts required
> L55: - **Zero selector maintenance**: Say goodbye to CSS selectors and XPath. Multimodal AI identifies page elements dir

## 星数曲线

```mermaid
xychart-beta
    title "MigoXLab/webqa-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 233 --> 237
    line [234, 235, 236]
```

2026-10-18 234 → 2026-10-24 236（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f11512b342da` · [字段定义](../../DATASET.md)*
