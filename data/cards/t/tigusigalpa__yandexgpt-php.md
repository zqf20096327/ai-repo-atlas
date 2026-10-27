# tigusigalpa/yandexgpt-php

⭐ 24 · PHP · MIT · 推送 2026-04-13 · [GitHub](https://github.com/tigusigalpa/yandexgpt-php) · 个人维护

**PHP 开发者接入 YandexGPT/YandexART API 的 SDK**

面向 PHP 8.0+ 项目的 YandexGPT 与 YandexART API SDK，支持文本生成、对话、图像生成（异步与同步封装）及 Conversations API 服务端对话管理；内置 Laravel Service Provider/Facade 与自动发现，也可在非 Laravel 项目中直接使用客户端。自动获取并刷新 OAuth/IAM 令牌（IAM 有效期 12 小时），支持 YandexGPT Lite/Pro、Alice AI 模型及推理模式（Reasoning Mode，仅 Pro 模型，尚不支持流式输出）。经 Composer 安装，云端资源管理依赖配套包 yandex-cloud-client-php。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 YandexGPT Lite/Pro/Alice AI 与 YandexART 图像生成
- Laravel 内置支持：Service Provider、Facade、自动发现
- OAuth→IAM 令牌自动获取与刷新（12 小时有效期）
- Conversations API 服务端对话与元素的完整增删改查

## 适用场景

- 在 PHP/Laravel 应用中集成 YandexGPT 文本生成与对话
- 构建带历史记录的聊天机器人或客服自动化
- 通过 YandexART 生成文章配图等内容图像
- 按推理模式处理需要逻辑推理的请求

## 场景标签

 · 领域:LLM 基础设施/API SDK

## 证据(README 行号)

> L12: PHP SDK для YandexGPT API и YandexART. Генерация текста, диалоги, изображения, Conversations API. Работает с любым 
> L27: - Laravel: Service Provider, Facade, конфигурация

## 星数曲线

```mermaid
xychart-beta
    title "tigusigalpa/yandexgpt-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5465001493c1` · [字段定义](../../DATASET.md)*
