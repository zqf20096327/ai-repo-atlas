# kweinmeister/agentitest

⭐ 48 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/kweinmeister/agentitest) · 个人维护

**用自然语言编写浏览器测试的 LLM 测试框架**

基于 pytest 的浏览器测试自动化框架：通过 browser-use 库将自然语言任务描述转换为浏览器操作，由 LLM agent 执行测试步骤；conftest.py 提供 llm 与 browser_session fixtures 及 run_agent_task 辅助函数，测试文件以自然语言定义场景与预期结果。执行后生成 Allure 报告，包含截图、agent 操作步骤、AI "thoughts" 及 OS/Python/浏览器版本等环境信息。安装依赖 uv sync，使用 Gemini API key，浏览器由 Playwright 提供 Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言任务代替选择器编写浏览器测试
- 基于 browser-use + pytest + Allure Report 的组合结构
- Allure 报告记录截图、agent 动作与 AI 思考过程
- 测试环境信息（OS/Python/浏览器版本）自动写入报告

## 适用场景

- 用自然语言编写并运行 Web 端到端测试
- 为社区网站等任意站点快速搭建可维护的测试套件
- 在 CI 中以 headless 模式运行并查看带步骤截图的测试报告

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: This framework uses an LLM to automate browser testing through high-level, natural language commands. It's designed 
> L7: * **`browser-use`**: Translates natural language into browser actions with an agent.
> L15: * **Natural Language Tests**: Write tests using descriptive, natural language tasks instead of brittle selectors.

## 星数曲线

```mermaid
xychart-beta
    title "kweinmeister/agentitest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-25 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b7ac53989b2d` · [字段定义](../../DATASET.md)*
